s = 'interview'
l = 'aeiou'
count = 0
ch = 0
for i in s.lower():
    if i in l:
        ch+=1
        #ch[i] = ch.get(i, 0)+1
print(ch)
