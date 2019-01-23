n, k = map(int,input().split())
x = list(map(int, input().split()))
flag =  0
for i in range(len(x)):
    for j in range(i, len(x)):
        if x[i]+x[j]==k:
            flag = 1
            break
        else:
            continue
if flag == 0:
    print("no")
else:
    print("yes")