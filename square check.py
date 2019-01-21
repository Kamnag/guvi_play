x = []
for i in range(4):
    x.append(list(map(int,input().split())))
if x[0][0]==x[1][0] and x[2][0]==x[3][0] and abs(x[0][1]-x[1][1])==abs(x[2][1]-x[3][1]):
    print("yes")
else:
    print("no")
    
