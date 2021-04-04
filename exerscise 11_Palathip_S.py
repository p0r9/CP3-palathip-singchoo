stair = int(input('stair : '))
for i in range (stair) :
    space = stair
    space -= i-1
    print ((space*' ')+('*'*2(i+1)))
