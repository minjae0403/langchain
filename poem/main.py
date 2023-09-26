import os, openai
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv(verbose=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

# play ground의 complete 모드로 자동 완성 기능을 제공해 준다.
# lim = OpenAI(openai_api_key=openai_api_key)

chat_model = ChatOpenAI(openai_api_key=openai_api_key)
content = "사랑"

# result = chat_model.predict(content+"와 관련된 단어 5개만 선택해줘")
# print(result)

import streamlit as st

st.title("AI 연관어 설정")

title = st.text_input("단어",)

if st.button("요청하기"):
    with st.spinner("생성중"):
        result = chat_model.predict(title + "와 연관된 단어 5개만 선택해줘")
        st.write("연관된 단어 5개 :")
        st.write(result)