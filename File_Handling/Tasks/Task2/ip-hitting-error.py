#Detect Failed Login Brute-Force (Advanced)
# The no. of times 401 error encounted by which IP.

import re
from collections import Counter 

file_name = "access.log"
count = Counter() #Counter is a dictionary-like object
pattern= re.compile(r"401")  #401 error
ip_pattern = re.compile(r"\b\d{1,3}(\.\d{1,3}){3}\b")

with open(file_name,'r') as file:
    for line in file:
        error = pattern.search(line)
        if error:
            error_pattern_logs = error.group() #group() returns the matched string
            #print(error_pattern_logs)
            count[(ip_pattern.search(line)).group()]+=1
    print(f"Count for 401 errors is as follows:\n{count}")

    for ip,count in count.most_common(1): #finds the top counts
        print(f"IP which hit max no. of times with 401 error is- {ip} and error is {count} times")
