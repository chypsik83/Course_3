from src.operation import get_correct_date, format_payment


def test_get_correct_date():
    """Проверка формирования отображения даты"""
    assert get_correct_date("2018-01-21T01:10:28.317704") == "21.01.2018"


def test_format_payment():
    """Проверка правильности форматирования счета"""
    assert format_payment("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert format_payment("Счет 35383033474447895560") == "Счет **5560"
    assert format_payment("") == "Данные отсутсвуют"
