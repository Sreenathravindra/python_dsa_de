def sliding_window(nums,k):
    left = 0
    window_sum = 0
    max_window= 0
    for right in range(len(nums)):
        window_sum = nums[right] + window_sum
        if right >= k-1:
            max_window = max(max_window,window_sum)
            window_sum = window_sum - nums[left]
            left+=1
    return max_window
if __name__ == '__main__':
    nums = [2, 1, 5, 1, 3, 2]
    k = 3

    a = sliding_window(nums,k)
    print(a)