import streamlit as st
## streamlit charts
## Plotting
# load iris.csv
# https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/iris.csv
st.set_option('deprecation.showPyplotGlobalUse', False)
import pandas as pd
iris_df = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/iris.csv")
st.subheader('dataframe of iris data')
st.dataframe(iris_df) #streamlit으로 dataframe 형태로 출력
#
st.subheader("Matplotlib/Pandas로 차트 그리기")
iris_df[iris_df['variety']=='Virginica']['petal.length'].hist()
#variety가 Virginica인 것에서 petal.length의 속성을 히스토그램으로 그리기
st.pyplot()

#dir로 확인 후 
#streamlit run iris-charts.py 로 실행