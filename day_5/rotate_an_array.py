def rotate_an_array(arr, k):
    n = len(arr)
    k = k%n
    return arr[k:]+arr[:k]


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 2
    print(rotate_an_array(arr,k))