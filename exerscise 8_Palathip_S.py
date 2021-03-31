Username = input('Username :')
Password = input('Password :')
if  Username == 'customer15'  :
    if Password == '12345678':
        print ('---DDsupermarket---')
        print ('Wellcome customer15')
        print ('Meat  50 THB/pack')
        print ('Egg   45 THB/dozen')
        print ('Water 35 THB/pack')
        print ('Milk  20 THB/pack')
        goods = input('goods what you will buy :')
        if goods == 'meat' or goods == 'Meat' :
             pack_1 = int(input('Number of piece'))
             Total_1 = pack_1*50
             print ('-------------------')
             print ('Total :',Total_1,'THB')
             print ('Thank you :D')
        elif goods == 'egg' or goods == 'Egg':
            dozen = int(input('Number of piece'))
            Total2 = dozen*45
            print ('-------------------')
            print ('Total :',Total2,'THB')
            print ('Thank you :D')
        elif goods == 'water' or goods == 'Water':
            pack2 = int(input('Number of piece'))
            Total3 = pack2*35
            print ('-------------------')
            print ('Total :',Total3,'THB')
            print ('Thank you :D')
        elif goods == 'milk' or goods == 'Milk':
            pack3 = int(input('Number of piece'))
            Total4 = pack3*20
            print ('-------------------')
            print ('Total :',Total4,'THB')
            print ('Thank you :D')
        else :
            print ('Error !!! ')
else :
    print ('Error !!!')