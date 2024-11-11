class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passengers(self,name):
        if not self.seat_available():
            return False
        self.passengers.append(name)
        return True
    
    def seat_available(self):
        return self.capacity - len(self.passengers)
    
