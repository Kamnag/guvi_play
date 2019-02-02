n = int(input())
x = list(map(int, input().split()))
s = 0
s+=n
x1 = list(set(x))
x1 = sorted(x1, reverse = True)
del x1[len(x1)-1]
a = len(x1)
for i in x1:
    s+=x.count(i)*a
    a-=1
print(s)
