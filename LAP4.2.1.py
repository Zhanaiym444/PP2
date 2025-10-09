import datetime

today = datetime.date.today()
five_days_ago = today - datetime.timedelta(days=5)
print("Current date:", today)
print("Five days ago:", five_days_ago)
