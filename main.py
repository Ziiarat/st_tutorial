import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
 
# Название
st.sidebar.title('Котировки компании Apple')
st.write("""
# Приложение о котировках компании Apple 

Показаны цены закрытия и объем продаж Apple

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2024-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Цена закрытия
""")
st.line_chart(tickerDf.Close)
st.write("""
## Объем продаж
""")
st.line_chart(tickerDf.Volume)
         
# Название
st.sidebar.title('Анализ чаевых')
st.write('Загрузка CSV файла')

uploaded_file = st.sidebar.file_uploader("Загрузите CSV файл с данными о чаевых", type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
else:
    st.stop()

#  # Функционал для скачивания графика чаевых
# if st.button('Скачать график чаевых'):
#     plt.savefig('tips_chart.png')
#     with open('tips_chart.png', 'rb') as f:
#         st.download_button('Скачать график', f, file_name='tips_chart.png')