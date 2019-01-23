t = int(input())
x = []
a = []
for i in range(t):
    x.append(list(map(int, input().split())))
for i in x:
    for z in i:
        a.append(z)
a = sorted(a)
for i in a:
    print(i, end = " ")
