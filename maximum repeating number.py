t = input()
n = list(map(int, input().split()))
max = 0
for i in n:
    if n.count(i)>max:
        a = i
        max = n.count(i)
print(a)