class Vehicles :
    Lisenumber = ''
    SerialCode = ''
    face = ''
    def TurnonAirconditioner (self):
        print ('Turn on : Air')

class Pickup(Vehicles) :    
    pass

class Car(Vehicles) :    
    pass

class Van(Vehicles) :    
    pass

class Estatecar(Vehicles) :    
    pass

car1=Car()
car1.TurnonAirconditioner()

van1=Van()
van1.TurnonAirconditioner()

pickup = Pickup()
pickup.TurnonAirconditioner()

estatecar = Estatecar()
estatecar.TurnonAirconditioner()