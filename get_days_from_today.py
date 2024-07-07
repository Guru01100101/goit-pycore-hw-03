from datetime import date
from typing import LiteralString


def get_days_from_today(str_date: str) -> int: 
    """Перетворює введену дату в форматі 'YYYY-MM-DD' в об'єкт date та обчислює різницю в днях між введеною датою та сьогоднішньою датою.

    Args:
        str_date (str): дата у форматі 'YYYY-MM-DD'

    Returns:
        int: цілочислена різниця в днях між введеною датою та сьогоднішньою датою. Якщо введена дата пізніша за сьогоднішню, функція повертає від'ємне число.

    Errors_handling:
        ValueError: якщо введена дата не відповідає формату 'YYYY-MM-DD'. Виводить повідомлення про помилку та пропонує ввести дату у правильному форматі.
    """
    today = date.today()
    
    try:
        converted_date = date.fromisoformat(str_date.strip()) # перетворення введеної дати в об'єкт date, для уникнення незначної помилки з пробілами на початку або у кінці рядка використовується метод strip()
        from_today = (today - converted_date).days
        return from_today
    except ValueError as e:
        print(e)
        return "Invalid date format. Please use the format 'YYYY-MM-DD'\nFor example: '2022-02-24'"
        

if __name__ == "__main__":
    str_date = input("Enter a date in the format 'YYYY-MM-DD': ")
    days = get_days_from_today(str_date)
    if isinstance(days, int):
        print(f"The date {str_date} is {days} days from today.")