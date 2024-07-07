from datetime import date, datetime
from get_days_from_today import get_days_from_today
from typing import TypedDict
import re


class User(TypedDict):
    name: str
    birthday: str

def days_to_upcoming_birthday(user: User) -> int:
    """Визначає кількість днів до наступного дня народження користувача.

    Args:
        user (User): словник з ім'ям користувача та його днем народження у форматі 'YYYY.MM.DD'

    Returns:
        int: кількість днів до наступного дня народження користувача
    """
    birthday = datetime.strptime(user['birthday'], "%Y.%m.%d").date() # перетворення рядка дати народження у об'єкт date
    today = date.today()
    birthday = birthday.replace(year=today.year) # заміна року на поточний
    if today > birthday: # якщо день народження вже минув у цьому році
        birthday = birthday.replace(year=today.year + 1) # заміна року на наступний
    return (birthday - today).days


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Alice Brown", "birthday": "1993.07.07"}
    ]
    for user in users:
        days = days_to_upcoming_birthday(user)
        if days > 0:
            print(f"{user['name']} has {days} days to the upcoming birthday.")
        else:
            print(f"{user['name']} celebrate the birthday today!")