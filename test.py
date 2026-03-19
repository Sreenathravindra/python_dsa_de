def freq_dict(nums):

    freq = {}
    for i in nums:
        freq[i] = freq.get(i,0) +1
    return freq


if __name__ =='__main__':

    nums = [1,1,2,3,3,3,4]

    a= freq_dict(nums)
    print(freq_dict)
