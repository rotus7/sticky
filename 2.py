arr = [i ** 2 for i in range(1, 129)]

target = int(input("Please enter id (1 to 128) : ")) - 1

tmp = arr[target]

for j in range(target):
    arr[target - j] = arr[target - j - 1]

arr[0] = tmp

print(arr)
