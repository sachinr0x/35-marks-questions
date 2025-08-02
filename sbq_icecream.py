'''
1. Python_SBQ_Icecream

Create a class Icecream with below attributes:
int - id
int - price
String - name
int - quantityInGms
String - category

Create the __init__ method which takes 
all parameters in the above sequence.
The method should set the value 
of attributes to parameter values inside 
the method.


Create a class IcecreamStore 
with below attributes:

String - IcecreamStoreName
List - IcecreamList

Create the __init__ method which takes 
all parameters in the above sequence.
The method should set the value of 
attributes to parameter values inside the method.

 

Implement two  methods - 
findMinimumIcecreamByPrice and 
sortIcecreamByid in IcecreamStore class.

 

findMinimumIcecreamByPrice-----
Create a method findMinimumIcecreamByPrice 
in the IcecreamStore class. This method 
will return the Icecream having the 
minimum value for price of all the 
Icecream in the Icecream List of the 
IcecreamStore class. If there is no 
Icecream found in the Icecream List 
or list is empty then return None to main program.

 
sortIcecreamByid-------
Create a method sortIcecreamByid in 
the IcecreamStore class. This method 
will return the sorted list of ids in 
ascending order of all the Icecreams in 
the IcecreamList of the IcecreamStore class. 
If there is no Icecream found in the 
Icecream List or list is empty, then 
return None to main program.

 

These methods should be called from 
the main method.

 

Instructions to write main section of the code:

a. You would require to write the main 
section completely, hence please follow 
the below instructions for the same.

b. You would require to write the main 
program which is inline to the sample 
input description section  mentioned 
below and to read the data in the same sequence.

c.  To create IcecreamStore and Icecream 
objects , take the inputs in below sequence.

    To create a List of n Icecream 
    objects read the value of n.

    To create a List of n Icecream 
    objects read values for id, price, 
    name, quantityInGms, category 
    (in this order) and create the 
    Icecream object and add to the 
    List. Repeat this step n times.

    Create the IcecreamStore object 
    passing the IcecreamStoreName and the 
    List of Icecreams created in previous 
    step.

d. Call the method findMinimumIcecreamByPrice 
using the IcecreamStore object created in 
point  #c. 

e. Call the method sortIcecreamByid using 
the IcecreamStore object created in point #c.

f. Print the output of both methods as per 
given sample output.

g. If there is NONE returned from any method 
print-"No Data Found."(without quotes)

 

Don't use any static text or formatting 
for printing the result. Just invoke 
the method and print the result.

Sequence for specific object will 
follow same attribute sequence as 
mentioned in the question. You may 
refer to the sample Input/output for 
the display format.
'''
 
class Icecream:

    def __init__(self, id1, price, name, quantityInGms, category):
        self.id1= id1
        self.price= price
        self.name= name
        self.quantityInGms= quantityInGms
        self.category= category

class IcecreamStore:
    def __init__(self, IcecreamStoreName, IcecreamList):
        self.IcecreamStoreName= IcecreamStoreName
        self.IcecreamList= IcecreamList

    def findMinimumIcecreamByPrice(self):
        price_list=[]

        for item in self.IcecreamList:
            price_list.append(item.price)

        min_price= min(price_list)

        for i in price_list:

            if i== min_price:
                return i
            elif price_list==[]:
                return None
            
    def sortIcecreamById(self):
        ids=[]

        for item in self.IcecreamList:
            ids.append(item.id1)
        ids.sort()

        if ids==[]:
            return None
        else:
            return ids
    
n= int(input())

IcecreamList=[]

for i in range(n):
    id1=int(input())
    price=int(input())
    name= input()
    quantityInGms= int(input())
    category= input()

    IcecreamList.append(Icecream(id1, price, name, quantityInGms, category))

ISObj= IcecreamStore("TCS", IcecreamList )

res1=ISObj.findMinimumIcecreamByPrice()
res2=ISObj.sortIcecreamById()

if res1==None:
    print("No Data Found")

else:
    print(id1)
    print(price)
    print(name)
    print(quantityInGms)
    print(category)

if res2== None:
    print("No Data Found")
else:
    for item in res2:
        print(item)


'''
Sample Input:

5
47
247
Vanilla
50
Mochi Icecream
61
877
Cookies n Cream
55
Gelato
90
310
Strawberry
45
Sorbet
24
620
Chocolate
30
Frozen Yogurt
54
163
Butterscotch
97
Rolled Icecream

 
Sample Output:

54
163
Butterscotch
97
Rolled Icecream
24
47
54
61
90

'''