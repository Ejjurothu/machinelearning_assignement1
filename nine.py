l=list(map(int,input("enter weights").split(" ")))
l1=[]
for i in l:
    l1.append(round(i*0.45359237,2))

print(l1)
