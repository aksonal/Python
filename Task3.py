#Task 3
#list manupulation
#Create a list of even and odd numbers.Identify even , odd numbers from the
#list and print them in separate list.Then put these two lists into dictionary

#program
List = [2,4,6,7,3,1]

#Empty lists
EvenList=[]
OddList=[]

total_1=0
total_2=0

# Iterate over the list
for value in range(0,len(List)):
   if (List[value] %2 ==0):
       EvenList.append(List[value])
       
   else:
       OddList.append(List[value])
     


print('Even numbers List is: ',EvenList)
print('Odd Numbers List is: ',OddList)

#Add all elements of each list
for value in range(0,len(EvenList)):
      total_1 = total_1 + EvenList[value]
      
for value in range(0,len(OddList)):
      total_2 = total_2 + OddList[value]

#dictionary
dict = {"Even Summation": total_1,"Odd Summation": total_2}
print(dict)

    
