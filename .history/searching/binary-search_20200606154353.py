import random

arr = []


def init_random():
    for i in range(50000):
        arr[i] = random.randint(1, 100000)


def binary_search(key):
    l = 0
    h = len(arr) - 1
    m = (l+h)/2
    while(l < h):
        if

def main():
    init_random()


if __name__ == '__main__':
    main()
