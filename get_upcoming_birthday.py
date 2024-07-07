from datetime import date, datetime
from typing import TypedDict


class User(TypedDict):
    name: str
    birthday: str

def days_to_congratulation(user: User) -> int:
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
    # Додаткова перевірка дня тижня. Якщо день народження у вихідний (субота або неділя), він переноситься на понеділок
    if birthday.weekday() in [5, 6]: # 5 - субота, 6 - неділя
        birthday = birthday.replace(day=birthday.day + (2 if birthday.weekday() == 5 else 1))
    return (birthday - today).days

def week_birthdays(users: list[User]) -> list[str]:
    """Визначає користувачів, які святкують день народження протягом наступного тижня.

    Args:
        users (list[User]): список словників з ім'ям користувача та його днем народження у форматі 'YYYY.MM.DD'

    Returns:
        list[str]: список імен користувачів, які святкують день народження протягом наступного тижня
    """
    today = date.today()
    week_birthdays = []
    for user in users:
        days = days_to_congratulation(user)
        if days >= 0 and days <= 7:
            congratulations_date = today.replace(day=today.day + days)
            user["congratulations_date"] = congratulations_date.strftime("%Y.%m.%d") # додавання дати вітання до словника користувача
            week_birthdays.append(user)
    return week_birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Alice Brown", "birthday": "1993.07.07"},
        {"name": "Bob Johnson", "birthday": "1995.07.13"}
    ]
    for user in users:
        days = days_to_congratulation(user)
        if days > 0:
            print(f"{user['name']} has {days} days to the upcoming birthday.")
        else:
            print(f"{user['name']} celebrate the birthday today!")
    week_birthdays_list = week_birthdays(users)
    if week_birthdays_list:
        print("Birthdays in the upcoming week:")
        for name in week_birthdays_list:
            print(name)
    else:
        print("There are no birthdays in the upcoming week.")