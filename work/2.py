# coding: utf-8

import const

const.MEMO_MAX_SIZE = 8

def moveForeArray(array):
    for i in range(len(array)):
        if array[i] == None:
            break

        else:
            i = const.MEMO_MAX_SIZE

    memoArrayCount = i

    s = input("Please set number in -> " + str(array) + " : ")

    select = int(s)

    idx = array.index(select)

    tmp = array[idx]

    for j in range(memoArrayCount - idx):
        array[idx + j] = array[idx + j + 1]

    array[memoArrayCount - 1] = tmp

    print(array)

def main():
    arr = [11, 22, 33, 44, None, None, None, None]

    moveForeArray(arr)

if __name__ == "__main__":
    main()
