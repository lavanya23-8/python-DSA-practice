arr = [1,2,3,4,5]
k = 2

k %= len(arr)
rotated = arr[-k:] + arr[:-k]
print(rotated)
