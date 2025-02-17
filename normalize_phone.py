import re


def normalize_phone(phone_number: str) -> str:
    """нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку (завжди повертає номер у форматі +380XXXXXXXXX)

    Args:
        phone_number (str): рядок номеру телефону у будь-якому форматі

    Returns:
        str: нормалізований номер телефону у форматі +380XXXXXXXXX

    Errors_handling:
        ValueError: якщо введений номер телефону не відповідає жодному з відомих форматів. Виводить повідомлення про помилку та пропонує ввести номер телефону у правильному форматі.
    """
    phone_number = re.sub(r'\D', '', phone_number) # видалення всіх символів, що не є цифрами
    if len(phone_number) == 10: # перевірка, чи введений номер телефону має 10 цифр
        return f"+380{phone_number}"
    elif len(phone_number) == 12 and phone_number.startswith("38"): # перевірка, чи введений номер телефону має 12 цифр та починається з '38'
        return f"+{phone_number}"
    else:
        raise ValueError("Invalid phone number format. Please use the format '0XXXXXXXXX' or '+38XXXXXXXXX'") 
    

if __name__ == "__main__":
    phone_number = input("Enter a phone number: ")
    try:
        normalized_phone = normalize_phone(phone_number)
        print(f"Normalized phone number: {normalized_phone}")
    except ValueError as e:
        print(e)
