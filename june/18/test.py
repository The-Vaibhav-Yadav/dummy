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

