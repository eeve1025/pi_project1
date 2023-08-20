import csv
import pandas as pd
import streamlit as st
import ffn

def getStockNames()->pd.Series:
        with open('codeSearch.csv',encoding='utf-8',newline='') as file:
                next(file)
                csv_reader = csv.reader(file)
                stock_codes = {}
                for item in csv_reader:
                #print(item)
                        key = item[2]
                        stock_codes[key] = item[3]
                #print(stock_codes)
        code_series:pd.Series = pd.Series(stock_codes)
        return code_series

stockName:pd.Series = getStockNames()
print(stockName)

def display_Data(dataFrame:pd.DataFrame,start_year) -> None:
    st.subheader(f'{start_year}~目前的歷史資料')  
    st.dataframe(dataFrame)
    st.subheader(f'{start_year}~目前的線圖')
    st.line_chart(dataFrame)

#多重選取
stockNames:pd.Series = getStockNames()
stock_name_id = stockNames.index.to_numpy() + "_" + stockNames.values #ndArray陣列相加
options = st.sidebar.multiselect('請選擇',
                   stock_name_id,
                   placeholder="股票:"  
                       )
names:list[str] = [] #建立符合ffn需要的股票名稱2330.TW
for name in options: 
    name_string = name.split('_')[0]
    names.append(name_string+".TW")

#prices = ffn.get(names, start='2010-01-01')
#print(prices)

