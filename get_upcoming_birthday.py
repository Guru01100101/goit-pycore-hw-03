from datetime import date
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
    birthday = re.sub(r"(\d{4})\.(\d{2})\.(\d{2})", r"\1-\2-\3", user['birthday']) # заміна крапок на тире для відповідності формату 'YYYY-MM-DD'
    today = date.today()
    birthday = f"{today.year}-{birthday[5:]}" # заміна року на поточний
    if today > date.fromisoformat(birthday): # якщо день народження вже минув у цьому році
        birthday = f"{today.year + 1}-{birthday[5:]}" # заміна року на наступний
    try:
        days = 0 - get_days_from_today(birthday) # функція get_days_from_today повертає від'ємне число, тому додаємо мінус для отримання додатнього числа
    except ValueError as e:
        print(e)
        days = "Invalid date format. Please use the format 'YYYY-MM-DD'\nFor example: '2022-02-24'"
    return days


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