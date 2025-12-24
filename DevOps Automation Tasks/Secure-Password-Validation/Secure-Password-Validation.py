
#take user input , password in string
import bcrypt

# ---------------- CONFIG ----------------
MIN_LENGTH = 10
SPECIAL_CHARS = set("@#$%")

def has_consecutive_chars(pwd):
    for i in range(len(pwd)-1):
        if pwd[i]==pwd[i+1]:
            return True
    return False

def one_upper(passwrd):
    return any(each_char.isupper() for each_char in passwrd)

def one_lower(passwrd):
    return any(each_char.islower() for each_char in passwrd)

def one_num(passwrd):
    return any(each_char.isdigit() for each_char in passwrd)

def one_special_char(passwrd):
    #return any(not each_char.isalnum() for each_char in passwrd)
    return any(c in SPECIAL_CHARS for c in passwrd)

def password_validation(pwd):
        if len(pwd) < MIN_LENGTH:
            raise ValueError(f"Password length should be atleast {MIN_LENGTH} characters in it")
        if not one_upper(pwd):
            raise ValueError("Password must have atleast 1 upper case character")
        if not one_lower(pwd):
            raise ValueError("Password must have atleast 1 lower case character")
        if not one_num(pwd):
            raise ValueError("Password must have atleast 1 digit")
        if not one_special_char(pwd):
            raise ValueError(f"Password must contain at least one special character {SPECIAL_CHARS}")
        if has_consecutive_chars(pwd):
            raise ValueError("Password must not have 2 consecutive same characters like (ss,##,11,AA)")
        return True

# ---------------- HASHING ----------------
def bcrypt_pass(pwd):

    #convert password to byte
    pass_in_bytes = pwd.encode('utf-8')

    #add salt and hass the byte password
    return bcrypt.hashpw(pass_in_bytes, bcrypt.gensalt())

user_pass = input("Please enter the password\nPassword should be of minimum 10 characters: ")

try:
    password_validation(user_pass)
    print("Passowrd Created Successfully")
    bcrypt_pass(user_pass)
except ValueError as e:
    print(f"Passowrd creation failed: {e}")
