from datetime import datetime
import os
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import pandas as pd
sns.set_theme()

i = input("Choose a date to plot: ").strip()
if i == "today":
    date = datetime.now().strftime("%Y-%m-%d")
else:
    date = i

if not os.path.exists(f"data/{date}.csv"):
    print(f'The file "data/{date}.csv" does not exist.')

df = pd.read_csv(f"data/{date}.csv", names=['time', 'weekday', 'count'])

df['time'] = pd.to_datetime(df['time'])

title = date + ' ' + df['weekday'][0]
df.plot(x='time',y='count', title=title)
time_format = mpl.dates.DateFormatter('%H')
plt.gca().xaxis.set_major_formatter(time_format)
plt.show()
