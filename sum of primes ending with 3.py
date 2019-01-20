def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	    return False
    return True

n = int(input())
s = 0
for i in range(n):
    if i%10 ==3:
        x = is_prime_number(i)
        if(x==True):
            s+=i
print(s)