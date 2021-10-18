import streamlit as st
st.header("Show data") 

## Load data
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris() 
st.write(iris.data) #객체.key값 <=> iris['data']
st.write(iris['target']) #0: 50개, 1: 50개, 2: 50개(스크롤 가능) <=> iris.target
st.write(iris.feature_names) #<=> iris['feature_names']

iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris['target'] #iris의 target 정보(0,1,2)를 새로 만듦(?)
iris_df['target'] = iris_df['target'].apply(lambda x: 'setosa' if x == 0 else ('versicolor' if x == 1 else 'virginica'))
#target이 0이라면 setosa, 1이라면 virsicolor, 2라면 virginica => 0,1,2 레이블의 이름 변경
 
## Return table/dataframe <데이터 시각화 방법 다름>
# table
st.table(iris_df) #.head()) #출력, target은 꽃의 실제 이름// 전부 다 보여줌
 
# dataframe
st.dataframe(iris_df) #11개(0~10)만 보여줌 + 스크롤바
 
st.write(iris_df) #데이터프레임과 비슷

st.header('Load diabetes data')
diabetes_df = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/diabetes.csv")
st.dataframe(diabetes_df)