n = int(input())
a = list(map(int,input().split()))
x = []
for i in range(len(a)):
    if(a[i]==i):
        x.append(a[i])
if(len(x)>0):
    x = sorted(x)
    for i in x:
        print(i, end=" ")
else:
    print(-1)
