
def pairSum(arr, s):
    # Write your code here.
    i = 0
    l   = []
    for j in range(1,len(arr)):

        if arr[i] + arr[j] == s:
            l.append((min(arr[i],arr[j]),max(arr[i],arr[j])))
        i+=1
    return l

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    s = 5
    print(pairSum(arr,s))