t = list(map(int, input().split()))
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
count = 0
for i in range(t[1]):
    if n2[i] in n1:
        continue
    else:
        count=1
if(count == 1):
    print("NO")
else:
    print("YES")