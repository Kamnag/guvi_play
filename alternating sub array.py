def fun1(a, i):
    if ((a[i] > 0 and a[i + 1] > 0) or (a[i] < 0 and a[i + 1] < 0)):
        return False
    else:
        return True


t = 1
for i1 in range(0, t):
    siz = int(input())
    a = map(int, input().split())
    a = list(a)
    b = [1] * siz
    for i in range(siz - 2, -1, -1):
        if (fun1(a, i)):
            b[i] = b[i + 1] + 1
    for i in b:
        print(i, end = " ")