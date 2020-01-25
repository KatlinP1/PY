list= [23,44,46,89,4,100,21,4003,76,4]
count=0
count2 = 0

for x in list:
    if x== 4:
        count +=1
    x = str(x)
    if x.find ("4") ==-1:
        count2 +=1
print (count)
print (count2)