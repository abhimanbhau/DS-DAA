def init_array(n, m):
    arr = []
    for i in range(n):
        arr.append(i * m)
    return arr


def main():
    arr1 = init_array(10, 1)
    arr2 = init_array(10, 2)
