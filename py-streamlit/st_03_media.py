import streamlit as st
st.header("Show media") # 오디오, 동영상, 이미지 출력

## Show image
## PIL : Python Image Library(파이썬 이미지 라이브러리)
## (How to install PIL): pip install pillow
from PIL import Image 

img = Image.open("files/example_cat.jpeg")
st.image(img, width=400, caption="Image example: Cat")
 
# media는 .read함수 사용

# ## Show videos
vid_file = open("files/example_vid_cat.mp4", "rb").read() #read함수로 열기
st.video(vid_file, start_time=2) #2초부터 시작
 
# ## Play audio file.
audio_file = open("files/loop_w_bass.mp3", "rb").read()
st.audio(audio_file, format="audio/mp3", start_time=10)

st.header("Load local image from PC") #pc에 있는 이미지 업로드
#### Load images
# Types of images
imgTypes = ["png", "jpg"]
 
st.info("Upload source image on Streamlit") #정보 보여주는 블록 설정
# # st.set_option('deprecation.showfileUploaderEncoding', False) #업데이트 된 버전은 사용안해도 됨
 
source_img_buf = st.file_uploader("Upload source image", type=imgTypes, key='src') #업로드되는 그림 파일 저장되는 메모리 객체// 그림 파일 저장 가능
 
if source_img_buf is not None: # 업로드하면 none이 아님
    source_img = Image.open(source_img_buf)
    #### Show image
    st.image(source_img)