def kadane_algo(nums):

    current_sum =nums[0]
    max_window_sum = nums[0]
    for i in range(1,len(nums)):
        current_sum = max(nums[i], current_sum+nums[i])
        max_window_sum = max(current_sum, max_window_sum)

        #caluculating sub_sec_array

    sub_sec_arry = sum(x for x in nums if x>0)
    if sub_sec_arry == 0:
        sub_sec_arry = max(arr)
    return  max_window_sum,sub_sec_arry


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    a = kadane_algo(nums)
    print(a)