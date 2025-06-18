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

#####

# prices = [10,1,5,6,7,1]

prices=[5,1,5,6,7,1,10]


if len(prices) == 2:
    if prices[-1] - prices [0] > 0:
        print( prices[-1] - prices [0])
    else:
        print( 0)

l = 0
ans = 0
for r in range(len(prices)):
    ans =  max((prices[r] - prices[l]), ans)
    if prices[l] > prices[r]:
        l = r
print((ans))

