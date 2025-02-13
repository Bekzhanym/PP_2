import datetime

today = datetime.date.today()
three_days_ago = today - datetime.timedelta(days=3)

n = today - three_days_ago
milli = n.total_seconds()*1000
print(milli*1000)