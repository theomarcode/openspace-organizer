from src.table import Table

class OpenSpace:
    """
    Represents an open space with multiple tables for seating guests.

    Args:
    number_of_tables (int): The total number of tables in the open space.
    number_of_seats_per_table (int, optional): The number of seats per table. Defaults to 5.
    """
    def __init__(self, number_of_tables, number_of_seats_per_table=5):
        """
        Constructor for the OpenSpace class.
        """
        self.tables = []
        for _ in range(number_of_tables):
            self.tables.append(Table(capacity=number_of_seats_per_table))
        self.number_of_tables = number_of_tables

    def organize(self, names):
        """
        Assigns guests to available seats in the open space.

        Args:
            names (list): A list of guest names.

        Raises:
            Exception: If the number of guests exceeds the total number of available seats.
        """
        if len(names) > sum(table.capacity_left() for table in self.tables):
            raise Exception("Insufficient seats")

        # Assign guests to tables one by one until all guests are seated
        while names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(names.pop())
                    break

    def display(self):
        """
        Displays the current seating arrangement of the open space.

        Prints a table layout showing the occupancy of each seat.
        """
        for i, table in enumerate(self.tables):
            print(f"Table {i}:")
            for j, seat in enumerate(table.seats, start=1):
                if seat.free:
                    print("-")
                else:
                    print(f"     Seat {j} - {seat.occupant}")

    def store(self, filename):
        """
        Saves the current seating arrangement to a file.

        Args:
            filename (str): The path to the file where the seating arrangement should be saved.
        """
        pass