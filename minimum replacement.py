n = int(input())
x = list(map(int,input().split()))
x1 = set(x)
print(len(x)-len(x1))