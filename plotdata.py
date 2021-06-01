import matplotlib.pyplot as plt
import seaborn
import pandas as pd

date = input("Choose a date to plot: ")
df = pd.read_csv(f"data/{date.strip()}.csv", names=['time', 'weekday', 'count'])

df.plot(x='time',y='count')
