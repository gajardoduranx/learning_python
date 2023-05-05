### Dates ###
# Representación de fechas, dias, horas, meses, años, etc
from datetime import datetime

now = datetime.now()

timestamp = now.timestamp() # Referencia el tiempo transcurrido desde 1970
print(timestamp)

year_2024 = datetime(2024, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print("Ahora")
print_date(now)
print("Otro año")
print_date(year_2024)

from datetime import time
## El time se debe trabajar encima, se le debe pasar información para trabajar con TIEMPO
current_time = time(1, 29, 44)

print(current_time.hour)
print(current_time.min)
print(current_time.second)

from datetime import date
## es similar a time pero en este caso se trabaja con FECHAS
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

## Operaciones con fechas
diff = year_2024 - now
print(diff)
diff = year_2024.date() - current_date
print(diff)

## Timedelta - nos ayuda a operar con franjas de fechas
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)