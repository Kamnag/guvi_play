# Sample bash code

def check(num):
    if num > 1:
   # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               return 0
            
       else:
           return 1
    else:
        return 0
       



for _ in range(int(input())):
    valar = int(input())
    s = input()
    s1 = ""
    for i in s:
        #print(check(i))
        
        if(check(ord(i))==1):
            s1=s1+i
        else:
            for j in range(ord(i),126+1):
                if(check(j)==1):
                    s1 = s1+chr(j)
                    break
    print(s1)
                  
                
