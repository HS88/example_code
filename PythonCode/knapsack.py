def Knapsack(value, weight, count, maxWeight):
    table = [[0]*(maxWeight+1) for i in range(count+1)]
    #print(table)
    
    for w in range( 1, maxWeight+1 ):
        #print(w)
        for i in range( 1, count+1 ):
            one = table[i-1][w]
            two = 0
            if(w - weight[i-1] >= 0 ):                
                two = table[i-1][w-weight[i-1]] + value[i-1]
            if one>two:
                table[i][w] = one
            else:
                table[i][w] = two
    #print(table)
    return(table[count][maxWeight])

a = Knapsack([1,3,6,2],[4,2,6,1],4,8)
print(a)
