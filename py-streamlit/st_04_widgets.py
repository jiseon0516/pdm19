import streamlit as st
st.header('Widgets')

## Widget
## Checkbox
if st.checkbox("Show/Hide"):
    st.text("체크박스가 선택되었습니다.")
    st.success('체크박스 선택 완료')
 
st.markdown("* * *") #밑줄 표시
 
 
## Radio button
status = st.radio("Select status.", ("Active", "Inactive"))
if status == "Active":
    st.success("활성화 되었습니다.")
else:
    st.warning("비활성화 되었습니다.")
 
 
st.markdown("* * *")
 
 
# Select Box (ex)
occupation = st.selectbox("직군을 선택하세요.",
                          ["Backend Developer",
                           "Frontend Developer",
                           "ML Engineer",
                           "Data Engineer",
                           "Database Administrator",
                           "Data Scientist",
                           "Data Analyst",
                           "Security Engineer"])
st.write("당신의 직군은 ", occupation, " 입니다.") #write함수로 출력
 
 
st.markdown("* * *")
 
 
## MultiSelect <중복 선택>
location = st.multiselect("선호하는 유투브 채널을 선택하세요.",
                          ("운동", "IT기기", "브이로그",
                           "먹방", "반려동물", "맛집 리뷰"))
st.write(len(location), "가지를 선택했습니다.")
 
 
st.markdown("* * *")
 
 
## Buttons
if st.button("About"):
    st.text("Streamlit을 이용한 튜토리얼입니다.")
 
 
st.markdown("* * *")
 
 
# Text Input <사용자 입력>
first_name = st.text_input("이름을 입력하세요.", "Type Here ...")
if st.button("Submit", key='first_name'):
    result = first_name.title()
    st.success(result)
 
 
# Text Area <두 줄 이상 입력>
message = st.text_area("메세지를 입력하세요.", "Type Here ...")
if st.button("Submit", key='message'):
    result = message.title()
    st.success(result)
 
 
st.markdown("* * *")
 
 
## Date Input
import datetime
today = st.date_input("날짜를 선택하세요.", datetime.datetime.now())
the_time = st.time_input("시간을 입력하세요.", datetime.time())
 
 
st.markdown("* * *")
 
 
# Display Raw Code - one line
st.subheader("Display one-line code")
st.code("import numpy as np") #연한 회색 배경
 
# Display Raw Code - snippet <코드 일부분 출력> -echo함수, ''' '''
st.subheader("Display code snippet")
with st.echo():
    # 여기서부터 아래의 코드를 출력합니다.
    import pandas as pd
    df = pd.DataFrame()
    df.head()
 
 
 
## Display JSON <파이썬 딕셔너리 구조 JSON 파일 출력>
st.subheader("Display JSON")
st.json({'name' : '민수', 'gender':'male', 'Age': 29}) #KEY:VALUE, KEY:VALUE 형식 출력
 
 
st.markdown("* * *")
 
 
## Sidebars
st.sidebar.header("사이드바 메뉴") #사이드바를 생성하고 헤더 붙이기
st.sidebar.selectbox("메뉴를 선택하세요.",
                    ["데이터",
                     "EDA",
                     "코드"])
st.sidebar.date_input("날짜를 선택하세요.", datetime.datetime.now(), key='new')

 
## streamlit charts
## Plotting
# load iris.csv
# https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/iris.csv
st.set_option('deprecation.showPyplotGlobalUse', False) #의미(?)
import pandas as pd
iris_df = pd.read_csv("https://github.com/Redwoods/Py/raw/master/pdm2020/my-note/py-pandas/data/iris.csv")
st.subheader('dataframe of iris data')
st.dataframe(iris_df)
#
st.subheader("Matplotlib/Pandas로 차트 그리기")
iris_df[iris_df['variety']=='Virginica']['petal.length'].hist() #virginica의 petal.length 속성 출력
st.pyplot()