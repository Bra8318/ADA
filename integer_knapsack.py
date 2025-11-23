# p = profit w = weight m = max_weight.
def knapsack(m,w,p):
    n = len(w)
    matrix = [[0]*(m+1) for _ in range(n+1)]
    #print(matrix)
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            else:
                #pick = 0
                if w[i-1]>j:
                    matrix[i][j] = matrix[i-1][j]
                else:
                    matrix[i][j] = max(p[i-1]+matrix[i-1][j-w[i-1]],matrix[i-1][j])
    return matrix[n][m]
    
            

m = 50
w = 10,20,30
p = 60,100,50
print("Maximum profit", knapsack(m,w,p))