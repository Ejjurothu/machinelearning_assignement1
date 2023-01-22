l=list(map(int,input("enter ages").split(" ")))
l.sort()
print(l)
min=min(l)
print("least number :",min)
max=max(l)
print("height number :",max)
l.append(min)
l.append(max)
print("after adding min and max to the list ",l)
if(len(l)%2==0):
    n=len(l)//2
    median=(l[n]+l[n-1])/2
else:
    median=l[len(l)//2]
print("median :",median)
avg=sum(l)/len(l)
print("avg :",avg)
range=max-min
print("range :",range)
