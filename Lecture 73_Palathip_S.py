systemMenu = {'ข้าวกระเพราหมู':30,'ข้าวกระเพราไก่':35,'ข้าวหมูกระเทียม':25,'ไข่ดาว':5}
menulist = []

def ShowBill():
    print ('---My Food---')
    price = 0
    for i in range(len(menulist)) :
        print (menulist[i][0],menulist[i][1])
        price += menulist[i][1]
    print ('Total :',price,'THB')

while True :
    MenuName = input('input your menu : ')
    if MenuName.lower() == 'exit' :
       break
    else :
        menulist.append([MenuName,systemMenu[MenuName]])
print (menulist)
ShowBill()