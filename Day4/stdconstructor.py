class student:
    
    def __init__(self,name,rollno,marks):
        self.name=name
        self.marks=marks
        self.rollno=rollno
    def display(self):
        print("======STUDENT DETAILS======")
        print("Name of the student=",self.name)
        print("Roll No=",self.rollno)
        print("Marks=",self.marks)
s1=student('Madhurika',584,100)
s1.display()
s2=student('Honey',555,99)
s2.display()