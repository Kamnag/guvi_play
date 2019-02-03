from itertools import combinations
s = input()
x = []
b = []
s = list(s)
for i in range(len(s)):
    x.append(combinations(s,i))
for i in x:
    for j in i:
        for k in range(len(j)-1):
            if ord(j[k])>ord(j[k+1]):
                print(j[k])
                continue
            else:
                break

