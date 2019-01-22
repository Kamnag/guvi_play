def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

t = input()
a = list(map(int,input().split()))
a = Remove(a)
count = 0
for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        if a[i]<a[j]:
            for k in range(j+1,len(a)):
                if a[j]<a[k]:
                    count+=1
                    # print(a[i],a[j],a[k])
                    # print(i,j,k)
print(count)