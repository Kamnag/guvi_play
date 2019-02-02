i=int(input())
A=[*range(2,i+1,2)]
B=[*range(1,i+1,2)]
print(len(A)+i)
print(*A,*B,*A)