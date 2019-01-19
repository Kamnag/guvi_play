a, b = input().split()
a, b = int(a), int(b)
x = []
for i in range(a):
    x.append(list(map(int, input().split())))
q = set.intersection(*[set(t) for t in x])
for m in q:
    print(m,end = " ")
