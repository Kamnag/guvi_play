t = int(input())
x = []
a = ""
j = 0
for i in range(t):
    x.append(list(input()))
x = [list(i) for i in zip(*x)]
for i in x:
    a+=i[0]
print(a)