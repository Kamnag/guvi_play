t = input()
n = list(map(int,input().split()))
count = 0
for i in n:
    if(n.count(i)>1):
        print(i)
        count+=1
        break
if(count == 0):
    print("unique")