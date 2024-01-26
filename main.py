#  from src.utils import hello
from src.openspace import OpenSpace



if __name__ == '__main__':
    """ The main entry point of the program. """
    excel_file = "colleagues.txt"
    # Read the contents of the "colleagues.txt" file into a list of colleagues.
    with open('colleagues.txt', 'r') as data:
        colleagues = data.readlines()
    # Remove any trailing whitespace from each colleague.
    colleagues = [colleague.strip() for colleague in colleagues]
    # Print the list of colleagues.
    print(colleagues)
    # Create an OpenSpace system with 5 tables.
    openspace = OpenSpace(number_of_tables=5)
    # Organize the colleagues into the tables.
    openspace.organize(colleagues)