g = [1,2]
s = [1,2,3]

g.sort()
s.sort()

p = 0
count = 0

for i in s:
    if p >= len(g):
        break
    if g[p] <= i:
        p += 1
        count += 1
    
        

print(count)


