from datetime import datetime, timedelta

users = [
    {'name': 'John', 'birthday': datetime(1990, 5, 12)},
    {'name': 'Jane', 'birthday': datetime(1995, 4, 3)},
    {'name': 'Alice', 'birthday': datetime(2000, 12, 30)},
    {'name': 'Bob', 'birthday': datetime(1985, 6, 2)},
    {'name': 'Carol', 'birthday': datetime(1992, 9, 21)},
    {'name': 'David', 'birthday': datetime(1988, 3, 8)},
    {'name': 'Eve', 'birthday': datetime(1999, 11, 1)}
]

def get_birthdays_per_week(users):
    today = datetime.now()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i in range(7):
        date = today + timedelta(days=i)
        print(weekdays[i] + ": ", end="")
        birthday_people = []
        for user in users:
            if user['birthday'].weekday() == date.weekday():
                birthday_people.append(user['name'])
        if len(birthday_people) == 0:
            print("No birthdays")
        else:
            print(", ".join(birthday_people))

get_birthdays_per_week(users)
