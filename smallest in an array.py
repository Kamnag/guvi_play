n, q = map(int,input().split())
x = list(map(int,input().split()))
y = []
for _ in range(q):
    y.append(list(map(int,input().split())))
for i in range(q):
    g = []
    u = y[i][0]
    v = y[i][1]
    for j in range(u-1,v):
        g.append(x[j])
    print(min(g))
    g = []

        
