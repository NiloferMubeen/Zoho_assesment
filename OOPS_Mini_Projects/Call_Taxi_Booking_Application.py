# TaxiBooking = display available cars, lend a car, update position after dropping, calculate fare
#customer = travel details,book a car

class TaxiBooking:
    
    def __init__(self,cars):
        
        self.cars = cars
        
        self.details = {'Taxi1':{'current':'A','earnings': 0},
                        'Taxi2':{'current':'A','earnings': 0},
                        'Taxi2':{'current':'A','earnings': 0},
                        'Taxi4':{'current':'A','earnings': 0}}
        
        self.distances = {'A': 0, 'B': 15,'C':30 ,'D':45,'E':60,'F':75}
        
        
    def lend_car(self,details):
        if len(self.cars) != 0:
            self.booked = self.cars.pop()
            self.details[self.booked]['current'] = details[1]
            self.details[self.booked]['earnings'] + self.calculate_fare(details)
            print('Your Taxi is booked')  
            return self.booked
        else:
            print('Sorry Taxi not Available')  
            
    
    def calculate_fare(self,details):
        distance = self.distances[details[1]] - self.distances[details[0]]
        if distance <= 5:
            return 100
        else:
            return 100 + ((distance - 5) * 5)
    
          
 
    def book_car(self):
        print('Pick up points \n 1. A \n 2. B \n 3. C \n 4. D \n 5. E \n 6. F')
        pickup = input('Enter your Pick up  point: ')
        print()
        destination = input('Enter your destination: ')
        return (pickup,destination)
    
    
    
taxi = TaxiBooking(cars=['Taxi1','Taxi2','Taxi3','Taxi4'])



print('-------------------------------------------------------')
print('           TAXI BOOKING APPLICATION                    ')
print('-------------------------------------------------------')

print('Enter 1 to book a car')

print('Enter 2 to exit')

user_choice = int(input('Enter an option:'))
while True:
    if user_choice == 1:
            details = taxi.book_car()
            taxi.lend_car(details)
            fare = taxi.calculate_fare(details)
        
            if fare : 
                print('------------------------')
                print('    BOOKING DETAILS')
                print('------------------------')
                
                print('Starting Point:',details[0])
                print('Destination   :',details[1])
                print('Distance(kms) :',taxi.distances[details[1]] - taxi.distances[details[0]])
                print('Total Amount  :',fare)
            
            else:
                print('Booking cancelled')

    if user_choice == 2:
        quit()   
   
   
   
    
    