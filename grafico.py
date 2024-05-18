import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv ('colombia-2016-01-22.csv')
df

from matplotlib import pyplot as plt
df.plot(kind='bar', x='region',y='samples_received', figsize=(10, 5), title='Casos de Zika recebidos na Colômbia em 2016')
columns = df.columns.tolist()
plt.xlabel("Regiões")
plt.ylabel("Casos")
plt.gca().spines[['top', 'right']].set_visible(False)
