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