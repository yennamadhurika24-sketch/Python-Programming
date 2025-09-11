class EmployeeDetails:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display1(self):
        print("====EMPLOYEE DETAILS====")
        print("Name of the employee=",self.name)
        print("Salary=",self.salary)
class Manager(EmployeeDetails):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display2(self):
        super().display1()
        print("Department=",self.department)
e1=EmployeeDetails('Madhurika',100000)
e1.display1()
e2=Manager('Madhurika',100000,'Data Analyst')
e2.display2()