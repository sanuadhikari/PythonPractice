p = float(input("enter the principle amount"))
t = float(input("enter time in years"))
if t>12:
    I = p*t*10/100
    print("interest",I)
else:
    I = p*t*15/100
    print("interst",I)