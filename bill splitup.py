n, k = map(int,input().split())
t = list(map(int,input().split()))
b = int(input())
a = t
del a[k]
s = 0
for i in a:
    s+=i
if s/2==b:
    print("Bon Appetit")
else:
    if(s>b):
        print(int(s/2-b)*-1)

    else:
        print(int(s/2-b))
