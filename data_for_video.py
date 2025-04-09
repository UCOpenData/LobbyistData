import pandas as pd
from datetime import date, timedelta

start_date = date(2014,1,1)
end_date = date(2024,12,1)
delta = timedelta(days=1)
while start_date <= end_date:
    print(start_date.strftime("%Y-%m-%d"))
    start_date += delta
activity = pd.read_csv('./datasets/LD_Lobbying_Activity.csv')
