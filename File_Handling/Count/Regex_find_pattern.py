# Detect all 5xx, ERROR, WARN logs using regex

import re

file_name = "app.log"
pattern_5xx= re.compile(r"\b5\d{2}\b") 

with open(file_name,'r') as file:
    for line in file:
        if "ERROR" in line or "WARN" in line or pattern_5xx.search(line):
            print(f"Line is: {line.strip()}") #strip() removes: \n (new line) & Extra spaces
