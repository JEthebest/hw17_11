from datetime import date


class Book:
    def __init__(self, ident, first_name, last_name, birth_date, profession):
        self.ident = ident
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.profession = profession
    
    def get_information(self):
        return f'ID: {self.ident}\nFirst_name: {self.first_name}\nLast_name: {self.last_name}\nBirth_date: {self.birth_date}\nProfession: {self.profession}'

c = Book(1, 'igor', 'pavlovich', date(day=11, month=11, year=1999), 'veterinar')
print(c.get_information())