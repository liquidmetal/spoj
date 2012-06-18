'''
Created on Jun 11, 2012

@author: utkarsh
'''

import sys

def calculateMaxFun(budget, fee, fun):
    numParties = len(fee)
    
    dp = []
    for i in range(numParties+1):
        temp = [0] * (budget+1)
        dp.append(temp)
        
    # Iterate over the parties
    for i in range(numParties):
        for b in range(budget+1):
            leftover = b - fee[i]
            above = dp[i][b]
            
            # We'd still have some room
            if leftover>=0:
                possible = dp[i][leftover] + fun[i]
                dp[i+1][b] = possible if possible>above else above
            else:
                dp[i+1][b] = above
                
    lastRow = dp[-1]
    lastFun = lastRow[-1]
    outputBudget = budget
    while(lastRow.pop()==lastFun):
        outputBudget-=1
        
    print("%d %d" % (outputBudget+1, lastFun))
                

while True:
    control = raw_input().split()
    
    budget = int(control[0])
    parties = int(control[1])
    
    if budget==0 and parties==0:
        sys.exit(0)
    
    fee = []
    fun = []
    
    while(parties>0):
        inp = raw_input().split()
        fee.append(int(inp[0]))
        fun.append(int(inp[1]))
        parties-=1
        
    calculateMaxFun(budget, fee, fun)
        
    raw_input()
    


if __name__ == '__main__':
    pass