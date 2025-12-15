from itertools import islice
n=3
with open('file.txt','r') as file:
    for line in islice(file,2,4):
        print(line.strip())
