def init_array(n):
    arr = []
    for i in range(n):
        arr.append(i)

    return arr


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=", ")
    print()


def reverse_array(arr):
    i=0,j = len(arr) - 1
    while (i < len(arr) - 1 and j >= 0) and i <= j:
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        i += 1
        j = 1
    return arr


def main():
    arr = init_array(10)
    print_array(arr)
    arr = reverse_array(arr)
    print_array(arr)


if __name__ == "__main__":
    main()
