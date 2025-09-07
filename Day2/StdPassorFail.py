# Student Details
def Std(a):
    if(a>=40):
        if(a<=50):
            print("C grade")
        elif(a>=51 and a<=70):
            print("B grade")
        elif(a>=71 and a<=80):
            print("A grade")
        else:
            print("Distinction pass")
    else:
        print("Fail")
Sname=input()
Snumber=int(input())
M1,M2,M3=map(int,input().split(" "))
total_marks=M1+M2+M3
Avg=total_marks/3

print("Student name=",Sname,"\n Roll Number=",Snumber,"\n Marks of 3 Subjects=",M1,M2,M3,"\n Total Marks=",total_marks,"\n Average of marks=",round(Avg,2))
print("Grade= ")
Std(Avg)