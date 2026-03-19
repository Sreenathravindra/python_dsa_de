# revese an string

s = 'amazon'
l = list(s)
j = (len(s)) - 1
for i in range((len(l)//2)):
    l[i],l[j] = l[j],l[i]
    j-=1

s = ''.join(l)
print(s)