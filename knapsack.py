# p = profit w = weight m = max_weight.
def knapsack(p,w,m):
    items = []
    for i in range(len(p)):
         items.append((p[i],w[i],p[i]/w[i]))

    items.sort(key=lambda x:x[2],reverse=True)
    profit = 0
    #j = profit k = weight.l= ratio(p/w)
    for j,k,l in items:
            if m > 0 and k <= m:
                m = m - k
                profit = profit + j
                print(profit,k)
            elif m > 0:
                profit = profit + j * (m / k)
            else:
                break

    return profit


p = 30,40,45,77,90
w = 5,10,15,22,30
m = 50
print("Total profit is : ",knapsack(p,w,m))
