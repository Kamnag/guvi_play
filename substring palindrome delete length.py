s = input()
x = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        x.append(s[i:j])
x = sorted(x, reverse=True, key=len)
# print(x)
for i in x:
    if i == i[::-1]:
        temp = i
        break
    else:
        continue
temp = list(temp)
s = list(s)
res = list(set(temp)^set(s))
print(len(res))
