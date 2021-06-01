import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_theme()

date = input("Choose a date to plot: ")
df = pd.read_csv(f"data/{date.strip()}.csv", names=['time', 'weekday', 'count'])

df.plot(x='time',y='count')
