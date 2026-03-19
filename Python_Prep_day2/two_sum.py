def two_sum(nums,k):

    fr= {}
    for j in range(len(nums)):
        x = k-nums[j]

        print(fr)
        if nums[j] in fr:
            return [fr[nums[j]],j]
        fr[x] = j


if __name__ == '__main__':
    nums = [2,7,11,15]
    k = 9
    print(two_sum(nums,k))