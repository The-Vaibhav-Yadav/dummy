# n = [2,-3,4,-2,2,1,-1,4]

# n = [2,-900, 90, -900, 4, 7, 80, -900]

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxs = nums[0]
sub = 0

for n in nums:
    if sub < 0:
        sub = 0
    sub += n
    maxs = max(maxs, sub)
        
print(maxs)