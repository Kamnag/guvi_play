from itertools import permutations

num = int(input())
a = [int(x) for x in str(num)]
perm = list(permutations(a))
s=""
x=[]
for i in perm:
    for j in i:
        s+=str(j)
    x.append(s)
    s = ""
x = set(x)
for i in x:
    print(i)