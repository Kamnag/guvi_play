t = input()
a = list(map(int,input().split()))
x = []
for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i]<=a[j]:
                break
        if j == len(a)-1:
            x.append(a[i])
if x[len(x)-2] < x[len(x)-1]:
    del x[len(x)-2]
for i in x:
    print(i,end=" ")
a = sorted(a)
print()
print(a[len(a)-1])
