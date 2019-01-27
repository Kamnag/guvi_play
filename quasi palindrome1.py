s = input()
count = 0
# print(s)
if s == s[::-1]:
    print("yes")
    exit()
for i in range(len(s)):
    if s[len(s)-i-1]=='0':
        count+=1
    else:
        break
for i in range(count):
    s = '0'+s
# print(s)
if s==s[::-1]:
    print("yes")
else:
    print("no")
