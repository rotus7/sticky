arr = [10, 20, 30, 40, 0, 0, 0, 0]
length = len(arr)

for i in range(length):
    if arr[i] == 20:
        target = i
    elif arr[i] == 0:
        i = i - 1
        break

tmp = arr[target]

for j in range(i - target):
    arr[j + target] = arr[j + target + 1]

arr[i] = tmp

print(arr)
