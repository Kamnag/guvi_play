n, m = map(int, input().split())
x = []
for i in range(n):
    x.append(list(map(int,input().split())))
for i in range(len(x)):
    x[i]=sorted(x[i])
x = [list(i) for i in zip(*x)]
for i in range(len(x)):
    x[i]=sorted(x[i])
x = [list(i) for i in zip(*x)]
print(x)