class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passesgers = []
        
    def add_passengers(self,name):
        if not self.open_seats():
         return  False
        self.passesgers.append(name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passesgers)
    
flight = Flight(3)     

people = ["Harry","Ron","Hermonian","Ginny"] 
 
for person in people:
    success = flight.add_passengers(person)
    if success:
        print(f"Added {person} to the flight")
    else:
        print(f"Seats not available")