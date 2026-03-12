def move_all_zeros(nums):
    j=0
    for i in range(len(nums)):
        if nums[i] !=0:
            nums[j],nums[i] = nums[i],nums[j]
            j+=1
    return nums






if __name__ == '__main__':
    nums = [0,1,0,3,12]

    a = move_all_zeros(nums)
    print(a)