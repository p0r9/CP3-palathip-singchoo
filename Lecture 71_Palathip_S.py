menulist = []
pricelist = []

def ShowBill():
    print ('---My Food---')
    for i in range(len(menulist)) :
        print (menulist[i],pricelist[i])

def Total() :
    print ('---Total Price---')
    price = 0
    for x in pricelist :
        price += x
    print ('total :',price,'THB')
    
while True :
    MenuName = input('input your menu : ')
    if MenuName.lower() == 'exit' :
        break
    else :
        MenuPrice = int(input('input price : '))
        menulist.append(MenuName)
        pricelist.append(MenuPrice)
ShowBill()
Total()