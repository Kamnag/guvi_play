q = input()
n = list(map(int,input().split()))
x = []
for i in range(len(n)):
    for j in range(i+1,len(n)):
        for k in range(j+1,len(n)):
            if n[i]+n[j]==n[k]:
                print(n[i],n[j],n[k], end = " ")
                print()
