#Generate Dictionary of Numbers and Their Squares
d = {}

def create_dict(item):
    for i in range(1,(item+1)):
        d.update({i:(i*i)})
create_dict(5)
print(d)
