

def two_sum(nums,target):
    seen ={}
    for i, k in enumerate(nums):
        compliment = target - k
        if compliment in seen:
            return [seen[compliment], i]
        seen[k] = i




if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    a = two_sum(nums, target)
    print(a)