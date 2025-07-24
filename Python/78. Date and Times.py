import datetime

date = datetime.date(2004, 2, 12)
today = datetime.date.today()

time = datetime.time(12, 30, 55)
now = datetime.datetime.now()
now1 = now.strftime("%H:%M:%S -- %d/%m/%Y")

print(date)
print(today)
print(time)
print(now)
print(now1)

target_datetime = datetime.datetime(2032, 1,2,12,00,00)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")