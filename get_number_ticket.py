from random import sample


def get_numbers_ticket(minimal: int, maximal: int, quantity: int = 5) -> list[int]:
    """Генерує список випадкових неповторюваних чисел у заданому діапазоні та кількості.

    Args:
        min (int): мінімальне значення числа не менше 1
        max (int): максимальне значення числа не більше 1000
        quantity (int): кількість чисел у списку (за замовчуванням 5)

    Returns:
        list[int]: список випадкових чисел у заданому діапазоні та кількості
    
    Errors_handling:
        ValueError: якщо min < 1, max > 1000 або quantity < 1 або quantity > max - min. повертає порожній список та виводить повідомлення про помилку.
    """
    if minimal < 1 or maximal > 1000 or quantity < 1 or quantity > (maximal - minimal + 1):
        print("Invalid input. Please make sure that 1 <= min < max, min < max <= 1000 and 0 < quantity <= max - min.")
        return []
    else:
        return sorted(sample(range(minimal, maximal + 1), quantity))
    

if __name__ == "__main__":
    minimal = int(input("Enter the minimal number: "))
    maximal = int(input("Enter the maximal number: "))
    quantity = int(input("Enter the quantity of numbers: "))
    ticket = get_numbers_ticket(minimal, maximal, quantity)
    print(f"Your ticket: {ticket}")