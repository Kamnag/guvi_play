q = input()
n = list(map(int,input().split()))
for i in range(len(n)):
    if i ==0:
        if n[i]%2==1:
            print(n[i], end = " ")
            continue
    if i%2==0:
        if n[i]%2 == 1:
            print(n[i], end = " ")
    if i%2==1:
        if n[i]%2 ==0:
            print(n[i], end = " ")