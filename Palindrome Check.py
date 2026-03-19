def Palindrome_Check(nums):


    for i in nums:
        s = list(i)
        fst = 0
        sec = len(i)-1
        while fst < (len(i)//2):
            s[fst],s[sec] = s[sec],s[fst]
            fst+=1
            sec-=1
            a = ''.join(s)

        print(i , '->',a == i)

if __name__ == '__main__':
    nums = ['madam','racecar','amazon']

    a=Palindrome_Check(nums)