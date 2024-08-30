from cs50 import SQL
from datetime import datetime

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

def calculate_age(year, month, day):
    today = datetime.today()
    return today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))

def get_birthdays():
    birthdays = db.execute("SELECT * FROM birthdays")
    for birthday in birthdays:
        birthday['age'] = calculate_age(birthday['year'], birthday['month'], birthday['day'])
        birthday['formatted_date'] = datetime(
            birthday['year'], birthday['month'], birthday['day']).strftime("%B %-d, %Y")
    return birthdays

def add_birthday(name, month, day, year):
    db.execute("INSERT INTO birthdays (name, month, day, year) VALUES(?, ?, ?, ?)",
               name, month, day, year)

def update_birthday(id, name, month, day, year):
    db.execute("UPDATE birthdays SET name = ?, month = ?, day = ?, year= ? WHERE id = ?",
               name, month, day, year, id)

def delete_birthday(id):
    db.execute("DELETE FROM birthdays WHERE id = ?", id)
