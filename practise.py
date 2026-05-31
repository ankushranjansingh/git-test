l = ['ankush', 'ranjan', 'singh', 'aman', 'singh', 'aman', 'singh']
counter = {}
for i in l:
    if i not in counter:
        counter[i] = 1
    else:
        counter[i] += 1

print(counter)