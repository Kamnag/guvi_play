def int_to_bin_string(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return str(s)

n = input()
x = list(map(int, input().split()))
a = []
final = []
for i in x:
    a.append(int_to_bin_string(i).count('1'))
m = zip(x,a)
for i in m:
    final.append(i)
final = sorted(final,reverse = True, key=lambda x: x[1])
for i in final:
    print(i[0])
