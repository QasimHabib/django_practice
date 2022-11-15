
# a = 50
# print("maximum number is", max(10,98,75,8,43))
# print("my name is: %s and roll number is: %s" %("Qasim Habib", 24))
# list = ['Qasim', 'Habib', 'Cs', 'Std']
# list.append('Ali')
#
# list.insert(2, "Zeeshan")
# print(list)

# person = {'name': "Qasim Habib", 'age': 25}
# print(person)
# person['gender'] = 'male'
# print(person)

# list1 = [1,2,3,4,5]
# newList = list(filter(lambda x: x % 2==0, list1))
#
# print("list1", list1)
# print("newList", newList)

# demo_file = open("textFile.txt", 'r+')
# print(demo_file.read())

# import os
#
# if(os.path.exists("textFile.txt")):
#     os.rename("textFile.txt", "newTextFile")
#     print("file name changed")
# else:
#     print("file doesnt exist")
from datetime import datetime, timedelta


def display(**argument):
    time_for_now = datetime.now()
    a = argument["time"]
    y = argument["year"] * 365 if argument.get('year') else 0

    match a:
        case "future":
            return time_for_now + \
                   timedelta(days=y + argument["days"] if argument.get('days') else y,
                             hours=argument["hours"] if argument.get('hours') else 0,
                             minutes=argument["minutes"] if argument.get('minutes') else 0)
        case "past":
            return time_for_now - \
                   timedelta(days=y + argument["days"] if argument.get('days') else y,
                             hours=argument["hours"] if argument.get('hours') else 0,
                             minutes=argument["minutes"] if argument.get('minutes') else 0)
        case "today":
            return time_for_now
        case default:
            return "Please insert correct time"


print(display(time="past", year=1, days= 10, hours=3, minutes=11))


# argument["hours"] if argument.get('hours') else 0


