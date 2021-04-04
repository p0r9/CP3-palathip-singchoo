stair = int(input('stair : '))
for i in range (stair) :
    #print(" " *(stair - i -1) + ("*" * (2 * i +1)))
    space = stair
    space -= i-1
    print ((space*' ')+('*'*(i+1)))