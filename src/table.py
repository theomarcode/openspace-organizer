class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
        if not self.free:
            raise Exception("Seat is already occupied")
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        if self.occupant is None:
            raise Exception("Seat is already free")
        name = self.occupant
        self.occupant = None
        self.free = True
        return name
    
class Table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.seats = []
        for _ in range(capacity):
            self.seats.append(Seat())

    def has_free_spot(self):
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False
    
    def display(self):
        for seat in self.seats:
            if seat.free:
                print("seat available")
            else:
                print("No seat available{name}")

    def capacity_left(self):
        return len(list(filter(lambda seat: seat.free, self.seats)))