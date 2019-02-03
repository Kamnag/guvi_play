def findSubarrays(arr, n):
    found = False
    lsum = 0
    for i in range(n - 1):

        lsum += arr[i]
        rsum = 0
        for j in range(i + 1, n):
            rsum += arr[j]

        if (lsum * (n - i - 1) == rsum * (i + 1)):
            found = True
            return "yes"

    # If no subarrays found
    if (found == False):
        return("no")

t = int(input())
x = list(map(int, input().split()))
print(findSubarrays(x, t))