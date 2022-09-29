
class Employee:

    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname +'.'+lname +'@company.com'
        print(self.email)
        print(pay)
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)

emp_1=Employee('Ram','Pantha',5000)
emp_2 = Employee('Shyam','Panday',10000)

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
