

class TaxiBooking:
    
    def __init__(self):
        
        self.cars = ['Taxi1','Taxi2','Taxi3','Taxi4']
        
        self.position = {'Taxi1':'A',
                         'Taxi2':'A',
                         'Taxi3':'A',
                         'Taxi4':'A'}
        
        self.earnings = {'Taxi1':0,
                        'Taxi2' :0,
                        'Taxi3' :0,
                        'Taxi4' :0}
        
        self.distances = {'A': 0, 'B': 15,'C':30 ,'D':45,'E':60,'F':75}
        
        
    def lend_car(self,details):
        
        if len(self.cars) != 0:
            self.booked = self.cars.pop()
            
        elif len(self.cars) == 0:
            nearest_car = []
            
            for key,val in self.position.items():
                dist = abs(self.distances[details[0]] - self.distances[val])
                if dist <= 15:
                    nearest_car.append(key)
            if len(nearest_car) == 0:
                self.booked = nearest_car
            else:
                minimum_earnings = {}
                for i in nearest_car:
                    minimum_earnings[i] = self.earnings[i]                
                                       
                sorted_earnings = [key for key,_ in sorted(minimum_earnings.items(),key=lambda item : item[1])]
                self.booked = sorted_earnings[0]
        else:
            print('Sorry Taxi not Available') 
            
        self.position[self.booked] = details[1]
        self.earnings[self.booked] + self.calculate_fare(details)
        print('Your Taxi is booked')  
        return self.booked
        
            
    
    def calculate_fare(self,details):
        distance = abs(self.distances[details[1]] - self.distances[details[0]])
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
    
    
    
taxi = TaxiBooking()



print('-------------------------------------------------------')
print('           TAXI BOOKING APPLICATION                    ')
print('-------------------------------------------------------')

while True:
    
        print('Enter 1 to book a car')

        print('Enter 2 to exit')

        user_choice = input('Enter an option:')

        if user_choice == '1':
                    details = taxi.book_car() # has pickup and destination
                    booked = taxi.lend_car(details)
                    fare = taxi.calculate_fare(details)
                
                    if fare : 
                        print('------------------------')
                        print('    BOOKING DETAILS')
                        print('------------------------')
                        
                        print('Starting Point:',details[0])
                        print('Destination   :',details[1])
                        print('Distance(kms) :',abs(taxi.distances[details[1]] - taxi.distances[details[0]]))
                        print('Booked Taxi   :',booked)
                        print('Total Amount  :',fare)
                        
                        print()
                        
                    
                    else:
                        print('Booking cancelled')

        elif user_choice == '2':
                quit()   
        
        else:
            print('Enter a valid option')
   
   
   
    
    