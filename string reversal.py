# t = int(input())
n = list(map(str,input().strip(" ").split()))
for i in n:
    print(i[::-1], end = " ")
