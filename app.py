# app.py

import streamlit as st
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# .envからAPIキーを読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LLMインスタンス作成（openai_api_keyは環境変数設定済みなら省略可能）
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# UI部分
st.title("専門家AIアシスタント")
st.markdown("あなたの質問に、選んだ専門家が答えます。")

# 専門家選択
expert = st.radio("相談したい専門家を選んでください：", ("医師", "弁護士", "キャリアコンサルタント"))

# ユーザー入力
user_input = st.text_input("質問を入力してください")

# ボタンが押されたら処理
if st.button("送信") and user_input:
    system_prompts = {
        "医師": "あなたは患者に優しく説明する臨床医です。",
        "弁護士": "あなたは法律を簡潔に説明する弁護士です。",
        "キャリアコンサルタント": "あなたは相談者の立場で助言するキャリアコンサルタントです。"
    }

    with st.spinner("考え中..."):
        messages = [
            SystemMessage(content=system_prompts[expert]),
            HumanMessage(content=user_input)
        ]
        response = llm.invoke(messages)
        st.success("回答:")
        st.write(response.content)