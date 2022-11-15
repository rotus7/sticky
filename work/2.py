import numpy as np


# 1から128までの整数を内包表記で作成
arr = [i for i in range(1, 129)]

# 配列のシャッフル
np.random.shuffle(arr)

# STDIN
s = input("Please enter id (1 to 128) : ")

# str -> int
select = int(s)

# 選んだ数字の探索　(idx = arr.index() でも可)
for j in range(len(arr)):
    if select == arr[j]:
        break;

# 対象をtmpに代入
tmp = arr[j]

# 配列の要素数に合わせてselectから-1する
target = select - 1

# 移動
for k in range(target):
    arr[target - k] = arr[target - k - 1]

# 配列の先頭に対象の数字を移動
arr[0] = tmp
