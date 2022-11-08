class Employee:
    leaves=5  #class variable
    pass
ankit=Employee()
ayush=Employee()

ankit.name="Ankit Dubey"
ankit.salary= 2000
ayush.name="Ayush Dubey"
ayush.salary= 4000
print(ankit.name," ",ayush.name,ankit.salary,ayush.salary)

leaves=2
print(Employee.leaves)
