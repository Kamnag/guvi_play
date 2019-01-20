s = input()
x = []
for i in s:
    if i in x:
        break
    x.append(i)
print(len(x))
