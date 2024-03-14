from datetime import datetime

from config import DIR_JSON
from src.utils import sorting_operations


def get_correct_date(new_date):
    """Функция возвращает коректную дату в соответствии с ТЗ"""
    date_new = datetime.fromisoformat(new_date)
    return datetime.strftime(date_new, "%d.%m.%Y")


def format_payment(info_payment):
    """Принимает счет и форматирует"""
    if info_payment:
        account = info_payment.split()
        if info_payment.startswith("Счет"):
            account_alpha = account.pop()
            account_alpha = f"**{account_alpha[-4:]}"
            account.append(account_alpha)
        else:
            account_alpha = account.pop()
            account_alpha = f"{account_alpha[0:4]} {account_alpha[4:6]}** **** {account_alpha[-4:]}"
            account.append(account_alpha)
        return " ".join(account)
    return "Данные отсутсвуют"


def operations_print():
    for item in sorting_operations(DIR_JSON)[:5]:
        print(f'\n{get_correct_date(item["date"])} Перевод организации\n'
              f'{format_payment(item.get("from"))} -> {format_payment(item["to"])}\n'
              f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}')
