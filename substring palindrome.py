s = input()
x = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        x.append(s[i:j])
x = sorted(x, reverse=True, key=len)
# print(x)
for i in x:
    if i == i[::-1]:
        print(i)
        break
    else:
        continue