
def get_largest(arr):
    largest = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    return largest


if __name__ == '__main__':
    arr = [8,9,8,8,9,2,7,5,5]
    largest = get_largest(arr)
    print("largest = ",largest)
    newlist = [e for e in arr if e != largest]
    print("second largest", get_largest(newlist))
