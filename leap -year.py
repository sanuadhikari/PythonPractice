n = int(input("enter the any year"))
if n%4==0:
    print("This is leap year")
    if n%100==0:
        print("this is leap year")
        if n%400==0:
            print("this is leap year")
else:
    print("this is not leap year")