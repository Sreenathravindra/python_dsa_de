def min_sub_arr(arr,target):
    min_arr = float('+inf')
    left  =0
    sum_arr = 0
    for right in range(len(arr)):
        sum_arr = sum_arr + arr[right]
        while sum_arr > target:
            sum_arr = sum_arr - arr[left]
            left+=1

            min_arr = min(min_arr, right-left+1)
    return min_arr

if __name__ == '__main__':
    arr = [2, 3, 1, 2, 4, 3]
    target = 7
    print(min_sub_arr(arr,target))