def primeCheck(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return False

a, b = map(int, input().split())
count = 0
for i in range(a,b+1):
    x = list("{0:b}".format(i))
    if primeCheck(x.count('1')) ==True:
        count+=1
print(count)
