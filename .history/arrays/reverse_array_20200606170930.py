arr = []


def init_array(arr):
    for i in range(10):
        arr.append(i)


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], "\n")

def main():
    init_array()
    print_array(arr)