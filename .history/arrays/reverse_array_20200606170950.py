arr = []


def init_array():
    arr = []
    for i in range(10):
        arr.append(i)

    return arr


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], "\n")


def main():
    arr = init_array()
    print_array(arr)
