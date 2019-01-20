t = input()
n = list(map(int,input().split()))
temp = sorted(n, reverse=True)
temp2 = sorted(n)
a = []
b = []
for i in range(len(temp)):
    a.append(temp[i])
    a.append(temp[len(temp)-i-1])
for i in range(len(temp)):
    b.append(a[i])
print(b)