nums = [1,2,3]

hmap = {}

for num, i in enumerate(nums):
    if i in hmap:
        print(True)
    else:
        hmap[i] = num

print(hmap)

