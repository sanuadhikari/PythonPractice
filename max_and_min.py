

def maxmin(arr,n):
    maximum = arr[0]
    minimum = arr[0]
    for i in range(1,n):
        if arr[i]>maximum:
            maximum = arr[i]

        elif arr[i]<minimum:
            minimum = arr[i]
    return[maximum,minimum]
if __name__ == '__main__':
    arr=[2,3,8,6,10,7]
    N = len(arr)
    answer = maxmin(arr,N)
    print("maximum",answer[0])

    print("minimum",answer[1])


















