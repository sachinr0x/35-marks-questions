class Employee:
    def __init__(self, emp_no, emp_name, leaves):
        self.emp_no= emp_no
        self.emp_name= emp_name
        self.leaves= leaves

class Company:
    def __init__(self, cName, emp_list):
        self. cName= cName
        self.emp_list= emp_list

    def leave_available(self, emp_no, leave_type):
        remaining_leaves=0

        for item in self.emp_list:
            if item.emp_no== emp_no:
                for k,v in item.leaves.items():
                    if k== leave_type:
                        remaining_leaves=v

        return remaining_leaves


    def leave_permission(self, empno, leave_type, num_of_leaves):
        available= self.leave_available(empno, leave_type)

        if available>=num_of_leaves:
            print("Granted")
        else:
            print("Rejected")


n=2
emp_list=[]
for i in range (n):
    
    emp_no= int(input())
    emp_name= input()
    leaves={'EL':0, 'CL':0, 'SL':0}

    for k,_ in leaves.items():
        leaves[k]=int(input())
    emp_list.append(Employee(emp_no, emp_name, leaves))

company_obj= Company('TCS', emp_list)

emp_id= int(input())
leave_type=input()
num_of_leaves= int(input())


rem=company_obj.leave_available(emp_id, leave_type)
print(rem)
company_obj.leave_permission(emp_id, leave_type, num_of_leaves)



          
           

        
        