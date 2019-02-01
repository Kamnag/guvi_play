def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def findGCD(arr, n):
    result = arr[0]
    for i in range(1,n):
        result = gcd(arr[i],result)
    return result


n, q = map(int, input().split())
x = list(map(int,input().split()))
a = []
b = []
for i in range(q):
    a.append(list(input().split()))
for i in a:
    # print(i[1])
    tet1 = int(i[0])
    tet2 = int(i[1])
    if tet1 == tet2:
        print(x[tet1-1])
    else:
        for j in range(int(i[0])-1,int(i[1])):
            b.append(x[j])
        print(findGCD(x, n))
        b = []