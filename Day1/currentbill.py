# Calculate current bill
cno=int(input("enter customer number="))
cname=(input("Enter customer name="))
pmr=int(input("Enter present month reading="))
lmr=int(input("Enter last month reading="))
tu=pmr-lmr
cbill=tu*3.80 # cost per each unit = 3.80
print("Customer Number=",cno,"\n Customer Name=",cname,"\n Present month reading=",pmr,"\n last month reading=",lmr)
print("Total number of units=",tu,"\n Total current bill=",cbill)