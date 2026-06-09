class Solution:
    def buy_sell_stock(arr):
        max_l = float('-inf')
        min_l = float('+inf')
        for i in arr:
            min_l = min(i,min_l)
            b_s_st = i - min_l
            max_l = max(max_l, b_s_st)
        return max_l

    if __name__ == '__main__':
        arr = [7,1,5,6,4,3]
        print(buy_sell_stock(arr))