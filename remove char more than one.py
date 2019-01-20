s = input()
x = []
z = ""
for i in s:
    x.append(i)
for i in x:
    if x.count(i)>1:
        continue
    else:
        z+=i
print(z)
