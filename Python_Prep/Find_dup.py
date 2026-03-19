
def dup(nums):
    fr ={}
    l = []
    for i in nums:

        fr[i] = fr.get(i,0)+1
    for i in fr:
        if fr[i] > 1:
            l.append(i)
    return l









if __name__ == '__main__':
    nums = [1,2,3,4,2,5,1,6,6]
    print(dup(nums))

