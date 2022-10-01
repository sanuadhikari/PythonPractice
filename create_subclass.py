class Employee:

    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname +'.'+lname +'@company.com'


    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
class developer(Employee):


    developer_1=Employee('Ram','Pantha',5000)
    developer_2 = Employee('Shyam','Panday',10000)
    print(developer_1.email)
    print(developer_2.email)
    print(developer_1.pay)
    print(developer_2.pay)
    print(Employee.fullname(developer_1))
    print(Employee.fullname(developer_2))
