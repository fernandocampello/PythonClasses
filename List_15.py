x = [5,2,3,10]
n = len(x)
sum = 0
for _x in x:
    sum = sum + _x
    '''sum + = _x'''
print(sum)

mean = sum/n
print(mean)

sse = 0
for _x in x:
    sse = sse + (_x - mean)**2
print(sse)
ssen = sse/n
std = ssen**0.5
print(std)
    
ssen1 = sse/(n-1)
stds = ssen1**0.5
print(stds)


x = [5,2,3,10]
n = len(x)
sum = 0
for i in range(n):
    sum += x[i]
print(sum)
