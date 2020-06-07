def init_array(n, m):
    arr = []
    for i in range(n):
        arr.append(i * m)
    return arr


def print_array(arr):
    for i in range(1, len(arr)):
        print(arr[i], end=", ")
    print()


def merge_sorted_arrays(arr1, arr2):
    arr3 = []
    i, j = 0
    while i < len(arr1) - 1 and j < len(arr2) - 1:
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1
        elif arr2[j] < arr[i]:
            arr3.append(arr2[j])
            j += 1
    return arr3


def main():
    arr1 = init_array(10, 2)
    print_array(arr1)
    arr2 = init_array(10, 7)
    print_array(arr2)
    arr3 = merge_sorted_arrays(arr1, arr2)
    print_array(arr3)


if __name__ == "__main__":
    main()
