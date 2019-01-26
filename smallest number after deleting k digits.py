from itertools import combinations
n, k = map(int,input().split())
n1 = str(n)
x = sorted(combinations(n1,len(n1)-k))
s = ""
for i in x[0]:
    s+=i
print(s)