'''You are building a simple E-commerce application in Python. The system should maintain a list of products available in the cart. Write a Python program to perform the following operations using Lists:
1.Add a product to the cart.
2.Remove a product from the cart 
3.Search for a product in the cart 
4.Display all products in the cart
5.Show the total number of products in the cart'''
def add(l1):
    
    prod=input("Enter a product to add:")
    l1.append(prod)
    print('Product', prod,' added to cart')
def remove(l1):
    prod=input("enter a product to delete=")
    if prod in l1:
        l1.remove(prod)
        print('Product',prod,' removed from the cart.')
    else:
        print('Product',prod,' not found in the cart.')
    
def search(l1):
    prod=input("enter a product to search:")
    if prod in l1:
        print('Yes,',prod,' is in the cart')
    else:
        print('Yes,',prod,' is not found')
def display(l1):
    for i in l1:
        print('cart=',i)
def total_prod(l1):
    print("Total products in cart=",len(l1))
def sorting(l1):
    l1.sort()
    print("Sorted successfully")
    for i in l1:
        print(i)
def clearing(l1):
    l1.clear()
    for i in l1:
        print(l1)
l1=['Phone','Tab']
print("Cart Operations:",
      "\n1. Add Product",
      "\n2. Remove Product",
      "\n3. Search Product",
      "\n4. Display Cart",
      "\n5. Count Products",
      "\n6. Sort",
      "\n7.Clear",
      "\n8.exit")
while True:
    ch=int(input("Enter your choice="))  
    
    if ch==1:
        add(l1)
        
    elif ch==2:
        remove(l1)
        
    elif ch==3:
        search(l1)
        
    elif ch==4:
        display(l1)
        
    elif ch==5:
        total_prod(l1)
        
    elif ch==6:
        sorting(l1)
    elif ch==7:
        clearing(l1)
    elif ch==8:
        exit(0)
    else:
        print("Please, choose in between 1-6")
        
    
        
    