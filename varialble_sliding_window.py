def variable_sw(arr,n):
    max_len = 0
    sum_arr = 0
    left = 0
    for i in range(len(arr)):
        sum_arr = sum_arr + arr[i]
        while sum_arr >= n:
            sum_arr = sum_arr-arr[left]
            left +=1
        max_len = max(max_len, i-left+1)
    return max_len

if __name__ == "__main__":
    arr =  [1, 2, 1, 0, 1, 1, 0,0,4]
    n = 4
    print(variable_sw(arr,n))