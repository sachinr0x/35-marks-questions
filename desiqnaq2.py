class Property:
    def __init__(self, ptype, pvalue, maxbisprice):
        self.ptype= ptype
        self.pvalue= pvalue
        self.maxbidprice= maxbisprice

class Tender:
    def __init__(self, buyernamet, ptypet, bidpricet):
        self.buyernamet= buyernamet
        self.ptypet= ptypet
        self.bidpricet= bidpricet


def bidproperty(propobj, tenderobj):
    result = []
    best_bids = {}

    # Step 1: Pick highest bid per property type
    for t in tenderobj:
        prop_type = t.ptypet.lower()
        if prop_type not in best_bids or t.bidpricet > best_bids[prop_type].bidpricet:
            best_bids[prop_type] = t

    # Step 2: Validate highest bids
    updated_properties = []
    for prop in propobj:
        ptype_lower = prop.ptype.lower()
        if ptype_lower in best_bids:
            tender = best_bids[ptype_lower]
            if prop.pvalue <= tender.bidpricet <= prop.maxbidprice:
                result.append(tender.buyernamet)
                continue  # Don't add this property to the updated list (it's sold)
        updated_properties.append(prop)  # Property not sold

    # Step 3: Update original property list
    propobj.clear()
    propobj.extend(updated_properties)

    return result
        

#main
n= int(input())
propobj=[]
for i in range(n):
    ptype= input()
    pvalue= int(input())
    maxbidprice= int(input())
    propobj.append(Property(ptype, pvalue, maxbidprice))

n2= int(input())
tenderobj=[]
for i in range(n2):
    buyernamet= input()
    ptypet= input()
    bidpricet= int(input())
    tenderobj.append(Tender(buyernamet, ptypet, bidpricet))

valid_buyers = bidproperty(propobj, tenderobj)

# Output results
if valid_buyers:
    for name in valid_buyers:
        print(name)
else:
    print("Property Not found")

# Print remaining properties
for p in propobj:
    print(p.ptype)


"""
4
House
500000
700000
Independent house
1000000
1200000
Land
4000000
5000000
flat
7000000
9000000
5
Susma
land
2000000
Gautam
land
4500000
Ankit
land
5000000
Rahul
flat
10000000
Deepak
Mall
800000000

Output 1:
Ankit
House
Independent house
flat

Input 2:
4
House
500000
700000
Mall
1000000
1200000
Land
4000000
5000000
flat
7000000
9000000
3
Ankit
land
2000000
Rahul
flat
890000
Kavi
mall
110000

Output 2:
Property Not found
House
Mall
Land
flat
"""