'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def f(n):
    temp = n
    sum = 0
    while(temp>0):
        r = temp%10
        if(r%2!=0):
            sum = sum+r
        temp = temp/10
    return(sum)
    
def g(n):
    temp = n
    sum = 0
    for i in range(1,temp+1):
        if(temp/i==0):
            sum = sum+f(i)
    print(sum)
    
t = int(input())
g(int(input()))
    
