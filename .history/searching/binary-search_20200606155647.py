import random

arr = []


def init_increasing():
    for i in range(5):
        arr.append(i+i)


def binary_search(key):
    l = 0
    h = len(arr) - 1
    while(l < h):
        m = (l+h)//2
        if arr[m] == key:
            return m
        elif key < arr[m]:
            h = m - 1
        elif key > arr[m]:
            l = m + 1
    return -1


def main():
    init_increasing()
    key = int(input('Enter key: '))
    while(key != -1):
        print(binary_search(key))
        key = int(input('Enter key: '))


if __name__ == '__main__':
    main()
