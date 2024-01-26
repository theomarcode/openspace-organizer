from src.table import Table

class OpenSpace:
    def __init__(self, number_of_tables, number_of_seats_per_table=5):
        self.tables = []
        for _ in range(number_of_tables):
            self.tables.append(Table(capacity=number_of_seats_per_table))
        self.number_of_tables = number_of_tables

    def organize(self, names):
        if len(names) > sum(table.capacity_left() for table in self.tables):
            raise Exception("Insufficient seats")

        while names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(names.pop())
                    break

    def display(self):
        for table, seats in enumerate(self.tables):
            print(f"Table {table+1}:")
            for seat in seats:
                if seat.free:
                    print("-")
                else:
                    print(f"{seat.occupant}")

    def store(self, filename):
        pass