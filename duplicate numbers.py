n = int(input())
a = list(map(int,input().split()))
x = []
for i in range(len(a)):
    if(a.count(a[i])>1):
        x.append(a[i])
print(sorted(set(x)))
