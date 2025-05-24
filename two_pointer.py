def two_pointer(arr, target):
    arr.sort()
    left,right = 0, len(arr)-1
    while left < right:
        if (arr[left] + arr[right]) == target:
            return [arr[left], arr[right]]
        elif arr[left] + arr[right] < target:
            left+=1
        else:
            right-=1
    return []

output = two_pointer([1,2,3,4,5], 3)
print(output) # [2, 5]
for i in output:
    print(i)

