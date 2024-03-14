import json
from datetime import datetime


def read_file(file_path):
    """Считывает json данные по транзакциям и возвращает список словарей"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def sorting_operations(file_path):
    """Возвращает отсортированный по датам список успешных транзакций"""
    all_info = read_file(file_path)
    new_list = []
    for change_date in all_info:
        if not change_date or change_date["state"] == "CANCELED":
            continue
        elif change_date["state"] == 'EXECUTED':
            new_list.append(change_date)

    new_list.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    return new_list
