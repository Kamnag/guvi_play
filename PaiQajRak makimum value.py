n, p, q, r = map(int,input().split())
x = list(map(int,input().split()))
a = []
for i in range(len(x)):
    for j in range(i, len(x)):
        for k in range(j, len(x)):
            a.append(p*x[i]+q*x[j]+r*x[k])
print(max(a))