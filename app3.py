# YouTube Walk Through: https://www.youtube.com/watch?v=8JwdenBGmEo&feature=youtu.be

def return_change(to_return, coins = [.01, .05, .10, .25, 1.0, 5.0]):
    flag = None
    for c in coins:
        if c == to_return:  return c
        if c < to_return:
            flag = c
    temp_balance = round(to_return - flag, 2)
    return [flag] + [return_change(temp_balance)]
    
            
result = return_change(4.33) # Highly nested iterable
print(result)


# Recursive function to flatten an iterable with arbitrary levels of nesting.
# https://stackoverover.com/a/14491059/3182843
def flatten(L):
    for  item  in  L :
        try:
            yield from flatten(item)
        except TypeError:
            yield item