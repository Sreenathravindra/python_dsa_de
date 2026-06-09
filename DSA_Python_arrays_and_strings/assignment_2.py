'''🔸 Q2: Count Vowels in String

Input: "engineering"
Output: 5

'''
def count_vowels(s):
    count = 0
    ch = ['a', 'e','i','o', 'u']
    for i in s:
        if i in ch:
            count +=1
    return count
if __name__ == '__main__':
    s = 'engineering'
    print(count_vowels(s))



