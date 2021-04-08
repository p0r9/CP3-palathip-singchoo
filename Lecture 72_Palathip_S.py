menulist = []

def ShowBill():
    print ('---My Food---')
    price = 0
    for i in range(len(menulist)) :
        print (menulist[i][0],menulist[i][1])
    print ('---Total Price---')
    for x in range(len(menulist)):
        price += menulist[x][1]
    print ('total :',price,'THB')
    
while True :
    MenuName = input('input your menu : ')
    if MenuName.lower() == 'exit' :
       break
    else :
        MenuPrice = int(input('input price : '))
        menulist.append([MenuName,MenuPrice])
print (menulist)
ShowBill()