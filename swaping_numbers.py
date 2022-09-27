n1 = int(input("enter the first number"))
n2 = int(input("enter the second number"))
n3 = int(input("enter the third number"))
print("before swaping",n1,n2,n3)
n1,n2,n3 = (n1+n2),(n2+n3),(n3+n1)
# swap and add first and second number
print("after swaping",n1,n2,n3)