def max_sub_array(arr, k):
    max_arr = sum(arr[:k])
    sum_arr = max_arr
    left = 0

    for right in range(k, len(arr)):
        sum_arr = sum_arr - arr[left] + arr[right]
        max_arr = max(max_arr, sum_arr)
        left += 1
    return max_arr


if __name__ == '__main__':
    arr = [2, 1, 5, 1, 3, 2, 6]
    k = 3
    print(max_sub_array(arr, k))
