lower_bound= int(input())
upper_bound= int(input())

def check_disarium (lower_bound, upper_bound):
    disarium_list=[]
    ranged=  upper_bound-lower_bound
    start= lower_bound

    for i in range(ranged+1):
        num=start
        num_str=str(num)
        sum=0
        for j in range (len(num_str)):
            digit= int(num_str[j])
            sum+= digit**(j+1)
        if sum==start:
            disarium_list.append(start)
        start+=1

    return disarium_list

result= check_disarium(lower_bound,upper_bound)
print(result)


        


        



