n = int(input())
a = sorted(list(map(int,input().split())), reverse = True)
s = ""
for i in a:
    s+=str(i)
s = int(s)
print(s)
