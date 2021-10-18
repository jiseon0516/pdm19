#pip list: 파이썬 모듈들 표시
#'pip install (streamlit)파이썬 모듈 이름'으로 설치
#streamlit --version
#conda activate base: base로
#streamlit: 웹 앱 만드는데 최적화, 웹브라우저에 출력


import streamlit as st
st.text("streamlit ver. : " + st.__version__) #text함수 이용해 버전 출력
#'streamlit run st_01_start.py' 출력 실행

# ## Text 
# ## Title
st.title('Streamlit Tutorial: start by pdm00, 이상훈')
# ## Header/Subheader
st.header('This is header')
st.subheader('This is subheader')
# ## Text
st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")

# ## Markdown
st.header('Markdown')
st.markdown('# header-1')
st.markdown('## header-2')
st.markdown('#### header-4')
st.markdown('###### header-6')
 
# # list
st.header('markdown: List')
st.markdown('- list1')
# st.markdown('list1')
st.markdown('- list2')
st.markdown('- list3\n'
            '   * inner list1\n'
            '   * inner list2\n'
            '       - inner_inner list\n')
 
# ## Message
st.info("End of first note: **text, markdown, latex**!") #info(문자): 색 있는 타이틀 바 - 문자 강조

## streamlit messages <안내 추가>
st.success("Successful") #초록
st.info("Information!") #밝은 하늘
st.warning("This is a warning") #노랑
st.error("This is an error!") #빨강
st.exception("NameError('Error name is not defined')") #빨강 - 에러의 일종

## Code block
st.header('Code block')
code1 = '''def hello():
    print("Hello, Streamlit!")''' #''' ''', """ """: 두 줄 이상의 문자열// 콜론 후 들여쓰기

st.code(code1, language='python') #코드가 파이썬 포맷으로, 회색 배경

code2 = '''
def add(a,b):
    return a+b
''' 

st.code(code2, language='python')

# ## Latex, raw
st.header('latex') #수식
st.latex(r"\alpha_n, \beta, \gamma, \cdots, \omega") #r: 특수코드 없는 문자열, _n:아래첨자 n, \:그리스어
st.latex(r"Y = \alpha + \beta X_i") #1차원 회귀식
# ## Latex-inline
st.markdown(r"회귀분석에서 오차는 다음과 같습니다 $e_i = y_i - \hat{y}_i$") #라텍스 inline 수식 - $안에 수식 넣기
# ## Mean squared error
st.subheader("Mean squared error")
st.markdown(r"#### $MSE = \frac{1}{N-1} \sum_{i=1}^{N-1} (y_i - \hat{y}_i)^2$")