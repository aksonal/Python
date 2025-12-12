#code to count the no. of times occurance of each element

t = (1, 2, 2, 3, 3, 3,4,4,4,4,5,5,5,5,5,5,5)
counts = {}

for items in t:
    counts[items] = counts.get(items,0)+1

print(counts)
