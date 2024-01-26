class Seat:
    """
    A class representing a seat in a table.

    Attributes:
    free (bool): Whether the seat is currently occupied.
    occupant (str): The name of the person occupying the seat, if any.

    Methods:
    set_occupant(name): Assigns the given name to the seat.
    remove_occupant(): Removes the name from the seat and returns it.
    """
    def __init__(self):
        """Initializes the seat with the free attribute set to True."""
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
        """
        Assigns the given name to the seat and sets the free attribute to False.

        Raises an exception if the seat is already occupied.
        """
        if not self.free:
            raise Exception("Seat is already occupied")
        self.occupant = name
        self.free = False

    def remove_occupant(self):
        """
        Removes the name from the seat and sets the free attribute to True.

        Raises an exception if the seat is already free.
        """
        if self.occupant is None:
            raise Exception("Seat is already free")
        name = self.occupant
        self.occupant = None
        self.free = True
        return name

class Table:
    """
    A class representing a table with a given capacity.

    Attributes:
    capacity (int): The number of seats at the table.
    seats (list): A list of Seat objects, one for each seat at the table.

    Methods:
    has_free_spot(): Checks whether there is a free seat at the table.
    assign_seat(name): Attempts to assign the given name to a seat at the table.
    display(): Prints a representation of the seat occupancy status.
    capacity_left(): Returns the number of free seats at the table.
    """
    def __init__(self, capacity):
        """Initializes the table with the given capacity."""
        self.capacity = capacity
        self.seats = [Seat() for _ in range(capacity)]
        for _ in range(capacity):
            self.seats.append(Seat())

    def has_free_spot(self):
        """Checks whether there is a free seat at the table."""
        return any(seat.free for seat in self.seats)

    def assign_seat(self, name):
        """
        Attempts to assign the given name to a seat at the table.

        Returns True if a seat is found and occupied, False otherwise.
        """
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return True
        return False

    def display(self):
        """
        Prints a representation of the seat occupancy status.

        Prints "seat available" for each free seat and "No seat available {name}" for each occupied seat.
        """
        for seat in self.seats:
            if seat.free:
                print("seat available")
            else:
                print("No seat available{name}")

    def capacity_left(self):
        """
        Returns the number of free seats at the table.

        Returns the length of the list of free seats.
        """
        return len(list(filter(lambda seat: seat.free, self.seats)))