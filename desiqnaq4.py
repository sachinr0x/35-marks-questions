class Fruits:
    def __init__(self, fruitid, fruitname, price, rating):
        self.fruitid= fruitid
        self.fruitname= fruitname
        self.price=price
        self.rating= rating

class Myclass:
    @staticmethod
    def function1(fobj, ip_int):
        maxlis=[]
        fobj.sort(key=lambda x:x.price, reverse= True)


        for i in fobj:
            if i.rating>ip_int:
                maxlis.append(i)

        if maxlis==[]:
            return 0
        else:
            return maxlis
        
n= int(input())
fobj=[]

for i in range(n):
    fruitid= int(input())
    fruitname= input()
    price= int(input())
    rating= int(input())
    fobj.append(Fruits(fruitid, fruitname, price, rating))

ip_int= int(input())

result= Myclass.function1(fobj, ip_int)

if result:
    for i in result:
        print(i.fruitid)
        break
else:
    print("No such Fruit")

        