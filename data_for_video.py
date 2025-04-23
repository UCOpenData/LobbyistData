import pandas as pd
from datetime import date, timedelta
import thefuzz as fuzz

start_date = date(2014,1,1)
end_date = date(2024,12,1)
delta = timedelta(days=1)
day_list = []
while start_date <= end_date:
    print(start_date.strftime("%Y-%m-%d"))
    day_list.append(start_date.strftime("%m %d %Y"))
    start_date += delta
    #print(start_date)
    
activity = pd.read_csv('./datasets/LD_Lobbying_Activity.csv')
activity['DATE'] = pd.to_datetime(activity['PERIOD_START'])
department_counts = activity['DEPARTMENT'].value_counts()
top_departments = department_counts[:15]
df = pd.DataFrame(index=top_departments.keys(), columns=day_list)
#df.insert(0, "Label", top_departments.keys())
print(top_departments.keys())
for day in day_list:
    for department in top_departments.keys():
        #df[day][department] = activity[(activity['DATE'] < date) | (activity['DATE'] == date)]["DEPARTMENT"].value_counts()[department]
        current_date = pd.to_datetime(day)  # convert day string to pandas datetime
        filtered = activity[activity['DATE'] <= current_date]
        value_counts = filtered["DEPARTMENT"].value_counts()
        #df[day][department] = value_counts.get(department, 0)
        df.loc[department, day] = value_counts.get(department, 0)
        print(department)
df.fillna(0, inplace=True)
df.insert(0, "Label", df.index)
df.reset_index(drop=True, inplace=True)
df.to_csv('empty.csv', index=False)