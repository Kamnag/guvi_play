s = input()
x = []
for i in s:
    if i !=" ":
        x.append(i.lower())
x = set(x)
if len(x)==26:
    print("yes")
else:
    print("no")