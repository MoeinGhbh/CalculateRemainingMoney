x = [1,2,5,10,20,50,100,200]
return_Money=[]
def calculate(pay,Money):
    remaind= (Money*100)-(pay*100)
    for i in reversed(x):
        res = remaind//i
        if res >=1:
            remaind = remaind-(res*i)
            return_Money.append([i,res])
    return return_Money

if __name__=='__main__':
    cal_cash =input('please enter your pay and money: ').split(' ')
    print(calculate(float(cal_cash[0]),float(cal_cash[1])))

