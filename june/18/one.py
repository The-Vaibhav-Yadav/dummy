points = [[10,16],[2,8],[1,6],[7,12]]

points.sort()

res = len(points)
prev = points[0]

for i in range(1, len(points)):
    curr = points[i]

    if curr[0] <= prev[1]:
        prev = [curr[0], min(prev[1], curr[1])]
        res -= 1
    else:
        prev = curr

print(res)



####


nums = [1,2,3]

hmap = {}

for num, i in enumerate(nums):
    if i in hmap:
        print(True)
    else:
        hmap[i] = num

print(hmap)


#### 
s = "racecar"
t = "carrace"

shmap = {}
thmap = {}

for i in range(len(s)):
    if s[i] in shmap:
        shmap[s[i]] += 1
    else:
        shmap[s[i]] = 1


for i in range(len(t)):
    if t[i] in thmap:
        thmap[t[i]] += 1
    else:
        thmap[t[i]] = 1    

if shmap == thmap:
    print(True)

