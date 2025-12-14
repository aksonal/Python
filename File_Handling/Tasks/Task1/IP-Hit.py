Extract Client IP Addresses

import re
from collections import Counter 

file_name = "access.log"
count = Counter() #Counter is a dictionary-like object
pattern= re.compile(r"\b\d{1,3}(\.\d{1,3}){3}\b") 

with open(file_name,'r') as file:
    for line in file:
        IPs = pattern.search(line)
        if IPs:
            ips = IPs.group() #group() returns the matched string
            count[ips]+=1
    print(f"IPs count is as follows:\n{count}")

    for ip,count in count.most_common(1):
        print(f"IP hit max no. of times is- {ip} and its hit {count} times")
