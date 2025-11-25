lst = list(map(int, input("Enter numbers: ").split()))
is_sorted = True

for i in range(len(lst)-1):
    if lst[i] > lst[i+1]:
        is_sorted = False
        break

print("Sorted" if is_sorted else "Not Sorted")
