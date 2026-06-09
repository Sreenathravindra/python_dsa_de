'''🔸 Q1: Find Second Largest Number

Input: [10, 5, 20, 8]
Output: 10 '''

def second_largest_element(arr):
    arr.sort()
    return (arr[len(arr)-2])

if __name__ == "__main__":
    arr = [10, 5, 20, 8]
    print(second_largest_element(arr))




