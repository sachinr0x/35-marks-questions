class Painting:
    def __init__(self, paintingid, paintername, paintingprice, paintingtype):
        self.paintingid= paintingid
        self.paintername= paintername
        self.paintingprice= paintingprice
        self.paintingtype= paintingtype

class Showroom:
    @staticmethod
    def gettotalpaintingprice(pobj, ip_ptype):
        totalprice= 0
        for i in pobj:
            if i.paintingtype.lower()== ip_ptype.lower():
                totalprice+=i.paintingprice

        if totalprice==0:
            return None
        else:
            return totalprice


    @staticmethod
    def getpainterwithmax(pobj):
        pdictt={}
        result=[]
        pobj.sort(key=lambda x:x.paintername)

        for i in pobj:
            if i.paintername in pdictt:
                pdictt[i.paintername]+=1
            else:
                pdictt[i.paintername]=1

        sorteddict= dict(sorted(pdictt.items(),key=lambda x:x[1], reverse=True))

        

        return sorteddict





n=int(input())
pobj=[]

for i in range(n):
    paintingid= int(input())
    paintername= input()
    paintingprice= int(input())
    paintingtype= input()
    pobj.append(Painting(paintingid, paintername, paintingprice, paintingtype))

ip_ptype= input()

res1= Showroom.gettotalpaintingprice(pobj, ip_ptype)
res2= Showroom.getpainterwithmax(pobj)
    
if res1 is None:
    print("Painting not found")
else:
    print(res1)

for k,_ in res2.items():
    print(k)
    break