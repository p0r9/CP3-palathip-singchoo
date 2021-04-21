class Customer :
    name  = ''
    lastname = ''
    age = 0

    def Addcart (self) :
        print ('Added to',self.name,self.lastname,'cart')

customer1 = Customer()
customer1.name = 'Thanachat'
customer1.lastname = 'stang'
customer1.Addcart()

customer2 = Customer()
customer2.name = 'Vasavat'
customer2.lastname = 'Thee-o'
customer2.Addcart()

customer3 = Customer()
customer3.name = 'Jirapat'
customer3.lastname = 'James'
customer3.Addcart()