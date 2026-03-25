def two_sum(arr, k):
    ch = {}

    for j in range(len(arr)):
        compliment = k - arr[j]

        if arr[j] in ch:
            return [ch[arr[j]],j]
        ch[compliment] = j

if __name__ == '__main__':
    arr = [2,7,11,15]
    k = 9
    print(two_sum(arr, k))


