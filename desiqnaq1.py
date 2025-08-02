class Person:
    def __init__(self, name, height, weight, bmi, bmi_status=""):
        self.name= name
        self.height= height
        self.weight= weight
        self.bmi= bmi
        self.bmi_status= bmi_status

class Society:
    def __init__(self, bmi_status, person_list):
        self.bmi_status= bmi_status
        self.person_list= person_list

    def calculatebmiandstatusbyname(self, ip_name):
        lis=[]
        for i in self.person_list:
            if i.name.lower()== ip_name.lower():
                for k,v in self.bmi_status.items():
                    if i.bmi<=v[1] and i.bmi>=v[0]:
                        i.bmi_status= k

                lis.append(i)
        return True

    def removeinvalidpersons(self, bmi_thold):
        invalid_list=[]

        for i in self.person_list:
            # self.calculatebmiandstatusbyname(i.name)
            if i.bmi< bmi_thold:
                invalid_list.append(i)

        return invalid_list


n= int(input())
person_obj=[]

for i in range(n):
    name= input()
    height= int(input())
    weight= int(input())
    bmi= round(weight/(height*height))
    person_obj.append(Person(name, height, weight, bmi))



n2= int(input())

bmi_status={}

for i in range(n2):
    k= input()
    v1= int(input())
    v2= int(input())
    minn=min(v1, v2)
    maxx=max(v1,v2)

    bmi_status[k]=[minn, maxx]



ip_name= input()
bmi_thold= int(input())

soc_obj= Society(bmi_status, person_obj)

result1= soc_obj.calculatebmiandstatusbyname(ip_name)
result2= soc_obj.removeinvalidpersons(bmi_thold)

if result1:
    print("BMI Status Updated")
else:
    print("No person was found with that name")

if result2==[]:
    print("No Invalid Person Exists")

else:
    for i in result2:
        print(i.name)
        print(i.bmi)