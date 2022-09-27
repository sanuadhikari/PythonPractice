n = int(input("enter a  number"))
n1 = n%10
n2 = (n//10)%10
n3 = n//100
rev = (n1*100+n2*10+n3)
print("reverse of three digit number is:",rev)