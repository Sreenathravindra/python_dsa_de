'''🔸 Q3: Remove Duplicates from Array

Input: [1, 2, 2, 3, 1]
Output: [1, 2, 3]'''

def remove_dup(arr):
    new = set()
    res = []
    for i in arr:
        if i not in new:
            new.add(i)
            res.append(i)
    return  sorted(res)

if __name__ == '__main__':
    arr =[100, 3, 17, 2, 99]
    print(remove_dup(arr))