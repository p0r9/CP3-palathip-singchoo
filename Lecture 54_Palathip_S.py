def login () :
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput  == "customer115"  and passwordInput == "12345678":
        return showMenu()
    else :
        print ('username or password Wrong !!')
        return login()
def showMenu () :
    print('Done !!! :D')
    print("----- mindShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect ()
def menuSelect () :
    userSelected = int(input(">> "))
    if userSelected == 1 :
        total_price = int(input('your totalprice : ')) 
        print (vatcalculate (total_price))
    else :
        return pricecalculate ()
def vatcalculate (totalprice) :
    vat = 7
    result = totalprice + (totalprice *7/100)
    return result
def pricecalculate () :
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print ( vatcalculate(price1+price2) )
login ()