t1=(1,2,4,3,4,5,5,6)
t=(1,21,7)
count=0
for i in t1:
    for j in range(i+1):
        if t1[i]==t1[j]:
            count=+1
print (count)
    
