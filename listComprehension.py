#DS and Algo in Python Excercises C-1.18

list =  []

for i in range(0,10,1):
    if i == 0:
        list.append(0)
    else:
        list.append(2 * ( ( list[i-1] / 2 ) + i) )
        
print(list)
