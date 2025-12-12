#Write a Python program to add an item to a tuple.
tup = 4,6,2,8,3,1
tup1 = (15,20,25)
print(f'Original tumple: {tup}')
tup = tup + (9,)
print(f"tuple after adding \"9\": {tup}")

tup = tup[:5] + tup1 + tup[:5] 
print(f"Final tuple : {tup}")
