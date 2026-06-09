class Solution:
    def list_slicing(arr):
        return arr[1::2] # slicing : arr[start:stop:step]
    if __name__ == '__main__':
        arr = [1,2,3,4,5,6,7,8,9,10]
        print(list_slicing(arr))