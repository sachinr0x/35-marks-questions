class Employee:
    def __init__(self, empId, empName, department, experience, isCertified, baseSalary):
        self.empId= empId
        self.empName= empName
        self.department= department
        self.experience= experience
        self.isCertified= isCertified
        self.baseSalary= baseSalary


class Solution(Employee):
    @staticmethod
    def function1(emp_obj, ip_department, ip_thold):
        count=0

        for item in emp_obj:
            if item.department.lower()==ip_department.lower() and item.baseSalary>= ip_thold and item.isCertified.lower()=="true":
                count+=1

        return count
    

    @staticmethod
    def function2(emp_obj, ip_dep):
        name_list=[]
        total_salary=0
        avg_salary=0
        n=0

        emp_obj.sort(key=lambda employee:employee.baseSalary, reverse=True)

        for item in emp_obj:
            if item.department.lower()==ip_dep.lower():
                total_salary+= item.baseSalary
                n+=1

        if n:
            avg_salary= total_salary/n

            for i in emp_obj:
                if i.department.lower()== ip_dep.lower() and i.baseSalary>avg_salary:
                    name_list.append(i.empName)

        return name_list
    

n= int(input())
emp_obj= []

for i in range(n):
    empId= int(input())
    empName= input()
    department= input()
    experience= input()
    isCertified= input()
    baseSalary= int(input())

    emp_obj.append(Employee(empId, empName, department, experience, isCertified, baseSalary))

ip_dep= input()
ip_thold= int(input())

result1= Solution.function1(emp_obj, ip_dep, ip_thold)
result2= Solution.function2(emp_obj, ip_dep)

print("message1", result1)


if result2== []:
    print("message2")
else:
    for i in result2:
        print(i)
