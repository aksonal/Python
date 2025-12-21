import os
import sys
import gzip
import shutil
import boto3
import requests
from datetime import datetime, timezone
from botocore.exceptions import ClientError

# ================= CONFIG =================
FILES_DIR = "/Users/techprescient/Downloads"
SIZE_THRESHOLD_KB = 3
BUCKET_NAME = "test-access1235778i9"
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

s3_client = boto3.client("s3")


# ================= UTILITIES =================
def send_slack_alert(message: str):
    if not SLACK_WEBHOOK_URL:
        print("⚠️ Slack webhook not configured")
        return

    try:
        response = requests.post(SLACK_WEBHOOK_URL, json={"text": message}, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Slack alert failed: {e}")


def exit_with_alert(message: str):
    send_slack_alert(message)
    sys.exit(0)


# ================= FILE HANDLING =================
def get_log_files(directory: str) -> list[str]:
    return [
        f for f in os.listdir(directory)
        if f.lower().endswith(".log") and os.path.isfile(os.path.join(directory, f))
    ]


def filter_large_files(files: list[str], directory: str) -> list[str]:
    large_files = []
    for file in files:
        size_kb = os.path.getsize(os.path.join(directory, file)) / 1024
        if size_kb > SIZE_THRESHOLD_KB:
            large_files.append(file)
    return large_files


def rotate_logs(files: list[str], directory: str) -> dict:
    """
    Returns:
        { original_log_path : rotated_log_path }
    """
    rotated = {}
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")

    for file in files:
        src = os.path.join(directory, file)
        dst = os.path.join(directory, f"{file}.{timestamp}")

        os.rename(src, dst)

        # recreate empty original log file
        open(src, "w").close()

        rotated[src] = dst

    return rotated


def compress_files(rotated_files: dict) -> dict:
    """
    Returns:
        { rotated_file_path : gz_file_path }
    """
    compressed = {}

    for rotated_path in rotated_files.values():
        gz_path = f"{rotated_path}.gz"

        try:
            with open(rotated_path, "rb") as src, gzip.open(gz_path, "wb") as dst:
                shutil.copyfileobj(src, dst)

            compressed[rotated_path] = gz_path

        except Exception as e:
            send_slack_alert(f"❌ Compression failed: {rotated_path}\n{e}")

    return compressed


# ================= S3 =================
def s3_file_exists(bucket: str, key: str) -> bool:
    try:
        s3_client.head_object(Bucket=bucket, Key=key)
        return True
    except ClientError as e:
        return e.response["Error"]["Code"] != "404"


def is_gzip_empty(file_path: str) -> bool:
    try:
        with gzip.open(file_path, "rb") as f:
            return f.read(1) == b""
    except OSError:
        return False


def upload_files_to_s3(compressed_files: dict):
    failed = {}

    for rotated_path, gz_path in compressed_files.items():
        object_name = os.path.basename(gz_path)

        if is_gzip_empty(gz_path):
            send_slack_alert(f"⚠️ Empty gzip file skipped: {object_name}")
            continue

        try:
            if s3_file_exists(BUCKET_NAME, object_name):
                print(f"Skipping existing file: {object_name}")
                continue

            s3_client.upload_file(gz_path, BUCKET_NAME, object_name)

            # cleanup only after success
            os.remove(gz_path)
            os.remove(rotated_path)

        except Exception as e:
            failed[object_name] = str(e)
            send_slack_alert(f"❌ Upload failed for {object_name}\n{e}")

    return failed


# ================= MAIN =================
def main():
    log_files = get_log_files(FILES_DIR)

    if not log_files:
        exit_with_alert("No log files found to rotate")

    large_files = filter_large_files(log_files, FILES_DIR)

    if not large_files:
        exit_with_alert("No log files larger than threshold")

    rotated_files = rotate_logs(large_files, FILES_DIR)
    compressed_files = compress_files(rotated_files)

    if not compressed_files:
        exit_with_alert("No files were compressed")

    failed = upload_files_to_s3(compressed_files)

    if failed:
        for f, reason in failed.items():
            send_slack_alert(f"❌ Upload failed:\n{f}: {reason}")
    else:
        send_slack_alert("✅ All log files rotated, uploaded & cleaned successfully")


if __name__ == "__main__":
    main()
