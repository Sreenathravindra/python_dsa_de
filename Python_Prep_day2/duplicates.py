#using dict
def duplicates(nums):
    fr= {}
    for i in nums:
        fr[i] = fr.get(i,0)+1
        if fr[i] == 2:
            return True
    return False


if __name__ == '__main__':
    nums= [1,2,3,4,5,1]
    print(duplicates(nums))