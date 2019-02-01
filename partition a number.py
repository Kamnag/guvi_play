n,a,b=map(int,input().split())
n = n//2
su=0
while(True):
    su+=a+b
    if n==su:
        print('YES')
    if su>n:
        break
print('NO')
