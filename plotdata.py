import matplotlib.pyplot as plt
import seaborn
import pandas as pd

date = input("Choose a date to plot: ")
df = pd.read_csv(f"{date}.csv", names=['time','count'])

df.plot(x='time',y='count')
