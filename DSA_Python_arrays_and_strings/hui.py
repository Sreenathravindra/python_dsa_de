s = 'Python'
s1 = list(s)

left, right = 0, len(s)-1

while right >= left:

    s1[right],s1[left] = s1[left], s1[right]
    left+=1
    right-=1

print(''.join(s1))