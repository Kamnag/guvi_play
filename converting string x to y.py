x, y=map(str,input().split())
s = 0
s+=abs(len(x)-len(y))
x1 = []
y1 = []
for i in x:
    x1.append(i)
for i in y:
    y1.append(i)
if(len(x1)>len(y1)):
    for i in range(s):
        del x1[len(x1)-1-i]
elif(len(x1)<len(y1)):
    for i in range(s):
        del y1[len(y1)-1-i]
for i in range(len(x1)):
    if x1[i]==y1[i]:
        continue
    else:
        x1[i] = y1[i]
        s+=1
print(s)