def VatCalculator (totalprice) :
    result = totalprice+(totalprice *7/100)
    return result
price = int(input('input your totalprice : '))
print (VatCalculator (price))