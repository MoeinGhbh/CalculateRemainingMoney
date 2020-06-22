denominations = [200,100,50,20,10,5,2,1]
# 100p is £1

def returnChange(change, denominations):
	# makes a list size of length denominations filled with 0
	toGiveBack = [0] * len(denominations)

	# goes backwards through denominations list
	# and also keeps track of the counter, pos.
	for pos, coin in enumerate(denominations):
		# while we can still use coin, use it until we can't
		while coin <= change:
			change = change - coin
			toGiveBack[pos] += 1
	return(toGiveBack)
			
print(returnChange(13, denominations))
# returns [0, 0, 0, 1, 1, 0, 0]
# 1x 10p, 1x 20p