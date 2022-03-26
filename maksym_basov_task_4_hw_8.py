# познакомиться с модулем datetime и написать программу с помощью lambda для
# возвращение текущего года, месяца , дня
# например результат должен быть таким
# import datetime
# now = datetime.datetime.now()
# .....ваш код))
# print(year(now))
# print(month(now))
# print(day(now))
import datetime

now = datetime.datetime.now()

year = lambda now: now.year
month = lambda now: now.month
day = lambda now: now.day

print(year(now))
print(month(now))
print(day(now))