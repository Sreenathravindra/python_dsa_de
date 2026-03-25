import time
def rotate_an_array_by_ele(arr,k):
    start = time.time()
    for i in range(k):
        l = len(arr)-1

        a =arr[0]
        arr.remove(arr[0])

        #arr.append(arr[0])
        arr.insert(l,a)
        print(start - time.time())
    return arr

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    k = 2
    print(rotate_an_array_by_ele(arr, k))
