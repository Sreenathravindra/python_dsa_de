def kadane_algo(nums):
    current_sum =nums[0]
    max_window_sum = nums[0]
    for i in range(len(nums)):
        current_sum = max(nums[i], current_sum+nums[i])
        max_window_sum = max(current_sum, max_window_sum)
    return  max_window_sum


if __name__ == '__main__':
    nums = [-1,-5]
    a = kadane_algo(nums)
    print(a)