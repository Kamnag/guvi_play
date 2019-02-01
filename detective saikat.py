n = int(input())
x = list(map(int,input().split()))
s = 0
for i in range(n):
    temp = x[0]
    if x[i]>temp:
        for j in range(i):
            s+=x[j]
print(s)