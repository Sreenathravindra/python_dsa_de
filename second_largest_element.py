def second_largest_element(arr):
    f_lar = float('-inf')
    s_lar = float('-inf')
    for i in arr:
        if i > f_lar:
            s_lar, f_lar = f_lar, i
        elif i > s_lar and i!= f_lar:
            s_lar = i
    return s_lar, f_lar
if __name__ == "__main__":
    arr = [50,15,30,30,20,40]
    print(second_largest_element(arr))