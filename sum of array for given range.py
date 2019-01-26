n, q = map(int,input().split())
x = list(map(int,input().split()))
for _ in range(q):
    s = 0
    a, b = map(int,input().split())
    for i in range(a-1,b):
        s+=x[i]
    print(s)
    s = 0