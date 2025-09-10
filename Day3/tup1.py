
def maximummarks(t1):
    max_marks = max(t1, key=lambda x: x[2])[2]
    print("Student(s) with maximum marks:")
    for student in t1:
        if student[2] == max_marks:
            print(student)
def morethan75(t1):
    print("students scored more than 75:")
    for i in t1:
        if i[2]>75:
            print(i)
    
t1=[]
for i in range(5):
    rollno=int(input("Enter roll number:"))
    name=input("Enter the name")
    marks=int(input("Enter marks:"))
    student=(rollno,name,marks)
    t1.append(student)
print(t1)
maximummarks(t1)
morethan75(t1)
 
        
    