s = list(map(str,input().split()))
count = 0
for i in s:
    if i[0].isupper()==True:
        continue
    else:
        count = 1
if(count==1):
    print("no")
else:
    print("yes")