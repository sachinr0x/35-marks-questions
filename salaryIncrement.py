class Employee:
    def __init__(self, empId, empName, empRole, empSalary):
        self.empId= empId
        self.empName= empName
        self.empRole= empRole
        self.empSalary= empSalary

    def increment_salary(self, sal_inc_perc):
        pass
    

class Orgnazitation:
    def __init__(self, org_name, emp_obj):
        self.org_name= org_name
        self.emp_obj= emp_obj

    def calculate_salary(self, ip_string, ip_number):
        returnable_obj=[]
        for employ in self.emp_obj:
            if employ.empRole== ip_string:
                employ.empSalary+= (ip_number/100)*employ.empSalary
                print(employ.empName)
                print(employ.empSalary)
        

n= int(input())

emp_obj=[]

for i in range(n):
    empId= int(input())
    empName= input()
    empRole= input()
    empSalary= int(input())

    emp_obj.append(Employee(empId, empName, empRole, empSalary))

ip_string=input()
ip_number= int(input())

org_obj= Orgnazitation('TCS', emp_obj)

org_obj.calculate_salary(ip_string, ip_number)








    
