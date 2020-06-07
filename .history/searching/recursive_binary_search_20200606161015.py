import random

arr = []


def init_increasing():
    for i in range(5):
        arr.append(i + i)


def binary_search(key, l, h):
    while l <= h:
        m = (l + h) // 2
        if arr[m] == key:
            return m
        elif key < arr[m]:
            binary_search(key, l, m - 1)
        elif key > arr[m]:
            binary_search(key, m + 1, h)
    return -1


def main():
    init_increasing()
    key = int(input("Enter key: "))
    while key != -1:
        print(binary_search(key, 0, len(arr) - 1))
        key = int(input("Enter key: "))


if __name__ == "__main__":
    main()
