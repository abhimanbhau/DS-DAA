def init_array():
    arr = []
    for i in range(10):
        arr.append(i)

    return arr


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], "\n")
        
def reverse_array(arr):
    i ,j = 0, len(arr) - 1
    while(i < len(arr)-1 and j >= 0):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        i += 1


def main():
    arr = init_array()
    print_array(arr)
    
