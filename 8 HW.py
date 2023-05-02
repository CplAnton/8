import datetime



users = [
    {'name': 'John', 'birthday': datetime.date(1990, 4, 26)},
    {'name': 'Alice', 'birthday': datetime.date(1995, 4, 28)},
    {'name': 'Jane', 'birthday': datetime.date(1985, 4, 29)},
    {'name': 'Carol', 'birthday': datetime.date(2000, 4, 30)},
    {'name': 'Eve', 'birthday': datetime.date(1978, 5, 1)},
    {'name': 'Mike', 'birthday': datetime.date(1991, 5, 2)},
    {'name': 'Sarah', 'birthday': datetime.date(1998, 5, 3)},
    {'name': 'Adam', 'birthday': datetime.date(1982, 5, 4)},
    {'name': 'Oliver', 'birthday': datetime.date(1996, 5, 5)},
    {'name': 'Emily', 'birthday': datetime.date(1975, 5, 6)},
    {'name': 'Ben', 'birthday': datetime.date(1987, 5, 7)}
]


def get_birthdays_per_week(users):
    current_date = datetime.datetime.now().date()
    week_end_date = current_date + datetime.timedelta(days=7)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays = {day: [] for day in weekdays}

    for user in users:
        name = user['name']
        birthday = user['birthday'].replace(year=current_date.year)

        if birthday < current_date:
            birthday = birthday.replace(year=week_end_date.year)

        # Перевіряємо, чи є день народження вихідним днем
        if birthday.weekday() in (5, 6):
            # Якщо день народження - у вихідний день, змінюємо дату на наступний понеділок
            days_until_monday = (7 - birthday.weekday()) % 7
            birthday += datetime.timedelta(days=days_until_monday)

        if birthday <= week_end_date:
            weekday = weekdays[birthday.weekday()]
            birthdays[weekday].append(name)

    for day in weekdays:
        if birthdays[day]:
            names = ", ".join(birthdays[day])
            print(f"{day}: {names}")
        

get_birthdays_per_week(users)