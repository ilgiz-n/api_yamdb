import datetime as dt


def validate_year(self, value):
    current_year = dt.date.today().year
    if value > current_year:
        raise ValueError('Исправьте год')
    return value
