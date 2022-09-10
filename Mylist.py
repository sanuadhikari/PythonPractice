salaries = [1500, 2000, 1200, 3200, 3500, 5000, 1900]
print("Salaries", "\t", "Citytax", "\t", "Netsalaries")
for salary in salaries:
    citytax = (salary * 10) / 100
    netsalary = (salary - citytax)
    print(salary,"\t\t" ,citytax,"\t\t" , netsalary)
