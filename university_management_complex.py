class professor:
    def __init__(self, profId, profName, subjectsDict):
        self.profId= profId
        self.profName= profName
        self.subjectsDict= subjectsDict

class University:

    @staticmethod
    def getTotalExperience(prof_list, ip_profId):
        sum=0
        isMatched=False
        for item in prof_list:
            if item.profId== ip_profId:
                isMatched=True

                for k,v in item.subjectsDict.items():

                    sum+=v

        if isMatched:
            print(sum)
        else:
            print('0')
    

    @staticmethod 
    def selectSeniorProfessorBySubject(prof_list, ip_subject):
        high_exp=0
        isAvailable=False

        for item in prof_list:
            for k,v in item.subjectsDict.items():
                if k.lower()==ip_subject.lower():
                    isAvailable=True
                    if high_exp<v:
                        high_exp=v
                        prof_id= item.profId
                        prof_name=item.profName
                        subjects_dict=item.subjectsDict

        if isAvailable:
            lis=[prof_id, prof_name, subjects_dict]
            print (lis)
        else:
            print("None")
        
n=int(input())
prof_list=[]

for i in range(n):
    profId= int(input())
    profName= input()
    subjectsDict={}
    for j in range(int(input())):
            subject=input()
            exp= int(input())
            subjectsDict[subject]=exp

    prof_list.append(professor(profId, profName, subjectsDict))
ip_profId= int(input())
ip_subject=input()

University.getTotalExperience(prof_list, ip_profId)
University.selectSeniorProfessorBySubject(prof_list, ip_subject)
        




                
'''
4
1
Shivakumar
3
Maths
10
Physics
10
Chemistry
10
2
Rajesh
4
MATHS
5
PHYSICS
5
CHEMISTRY
5
COMPUTERS
5
3
vasudev
2
MATHS
4
PHYSICS
4
4
Srinivas
3
Maths
8
Physics
8
Chemistry
8
3
maths
'''
        
