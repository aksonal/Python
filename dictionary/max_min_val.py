#find max and min value of python dict

my_dict = {'x':500, 'y':5874, 'z': 560}

key,max_val = max(my_dict.items(),key=lambda item: item[1])
key,min_val = min(my_dict.items(), key=lambda item: item[1])

print(f"Max key value pair is: {key}:{max_val}")
print(f"Min key value pair is: {key}:{min_val}")
