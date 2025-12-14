#Python code to read no. of times ERROR, WARN or INFO log lines (short files)

count = 0
with open('app.log','r') as file:
# file.write("Hello Worldies!!!")
    for line in file:
        if "WARN" in line:
          count+=1

print(count)
