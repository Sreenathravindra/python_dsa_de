def duplicates_first(nums):
    fr = {}
    for i in nums:
        fr[i] = fr.get(i,0)+1
        if fr[i] == 2:
            return {'first_duplicate': i}

if __name__ == '__main__':
    nums= [3,1,4,2,1,3]
    print(duplicates_first(nums))