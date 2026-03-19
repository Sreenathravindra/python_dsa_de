l = [912,10,5,20,15,30,90]
max_num = l[0]
j = 1
for i in l:
    if max_num < i:
        max_num = i
    j+=1

print(max_num)