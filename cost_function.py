import numpy as np
x=np.array([1,2,3])
y=np.array([1,2,3])
# w=float(input())
# b=float(input())
# y_head=0
# cost_final=0
# for i in range(0,3):
#     y_head=w*x[i]+b
#     cost=((y_head-y[i])**2)/(len(x)*2)
#     cost_final+=cost
# print(cost_final)
b=0
cost_min=1000000000
w_best=0
cost_final=0
for w in np.arange(-1,3,0.1):
    for i in range(0,3):
        y_head=w*x[i]+b
        cost=((y_head-y[i])**2)/(len(x)*2)
        cost_sum+=cost
        if cost_sum<=cost_min:
            cost_min=cost_sum
print(cost_min,w_best)
