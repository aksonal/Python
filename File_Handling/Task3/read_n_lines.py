#itertools is a built-in Python module
#islice() = iterator slicing

from itertools import islice
n=3
with open('file.txt','r') as file:
    for line in islice(file,n):
        print(line.strip())
