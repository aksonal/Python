#Task 5
#create different classes and write main program to implement the operations

#define a class
class Employee:
    def __init__(self,Emp_Id,Name,Age):
        
        self.Emp_Id = Emp_Id
        self.Name = Name
        self.Age = Age

    def disp(self):
        
        print('Employee Details: ')
        print('Employee ID =',self.Emp_Id)
        print('Employee Name =',self.Name)
        print('Employee Age =',self.Age)
        print('\n')
        


class Course:
    def __init__(self,Course_id,Course_name,Course_duration):
        self.Course_id = Course_id
        self.Course_name = Course_name
        self.Course_duration = Course_duration

    def Add(self):
        print('The ',self.Course_id ,'course is of ',self.Course_name,' for ',self.Course_duration,' hours')


class Trainee(Employee):
    def __init__(self,Emp_Id,Name,Age,Trainee_id,Score):
        self.Trainee_id = Trainee_id
        self.Score = Score

        # invoking the __init__ of the parent class  
        Employee.__init__(self,Emp_Id,Name,Age)
        
    def show(self):
        
        print('Trainee Details: ')
        print('Employee ID =',self.Emp_Id)
        print('Trainee ID =',self.Trainee_id)
        print('Trainee Score =',self.Score)
        print('\n')

        

    def add(self,course_nm,Value,dictionary={}):
        self.course_nm = course_nm
        self.Value = Value
        self.dictionary= {}
        dictionary[course_nm]=Value
        #print('Dictionary => ', dictionary)
        return dictionary

    def Update(self,Dict,Status):
        self.Dict = Dict
        self.Status = Status
        d1 = {'Math':'Complete'}
        Dict.update(d1)
        return Dict
    

#employee object
#emp = Employee(1,'Angad',25)

#Trainee object
Trainee_Obj = Trainee(1,'Angad',25,101,20)
Trainee_Obj.disp()
Trainee_Obj.show()

#Course object
Course_Obj1 = Course(1,'Science',2)
Course_Obj1.Add()
Trainee_Obj.add('Science','Complete')
Course_Obj2 = Course(2,'Math',4)
Course_Obj2.Add()
Trainee_Obj.add('Math','Incomplete')
Course_Obj3 = Course(3,'Eng',3)
Course_Obj3.Add()
Trainee_Obj.add('Eng','Incomplete')
Course_Obj4 = Course(4,'Civics',1)
Course_Obj4.Add()
Trainee_Obj.add('Civics','Complete')
Course_Obj5 = Course(5,'EVS',2)
Course_Obj5.Add()
Dict = Trainee_Obj.add('EVS','Complete')
print('\n')
print('Original Dictionary => ',Dict)

Trainee_Obj.Update(Dict,'complete')
print('\n')
print('Updated Dictionary => ',Dict)



