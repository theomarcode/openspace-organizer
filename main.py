#  from src.utils import hello
from src.table import Table
from src.openspace import OpenSpace



if __name__ == '__main__':
    excel_file = "colleagues.txt"
    with open('colleagues.txt', 'r') as data:
        colleagues = data.readlines()
    colleagues = [colleague.strip() for colleague in colleagues]
    print(colleagues)
    openspace = OpenSpace(number_of_tables=5)
    openspace.organize(colleagues)