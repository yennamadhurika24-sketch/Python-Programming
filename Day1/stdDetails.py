# Student Details
Sname=input()
Snumber=int(input())
M1,M2,M3=map(int,input().split(" "))
total_marks=M1+M2+M3
Avg=total_marks/3
print("Student name=",Sname,"\n Roll Number=",Snumber,"\n Marks of 3 Subjects=",M1,M2,M3,"\n Total Marks=",total_marks,"\n Average of marks=",round(Avg,2))