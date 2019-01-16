# Duas maneiras de criar uma matriz


'''R = []
r = [0,0]
R.append(r)
R
[[0, 0]]
print(R)'''




'''R = []
R = [i for i in range(2)]
print(R)'''
  
    
####################################################


#R = []
R = [[input("número: ") for i in range(2)]for j in range(2)]
print(R)


R = [[float(input("número: ")) for i in range(2)]for j in range(2)]
print(R)
