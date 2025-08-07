import streamlit as st
from dotenv import load_dotenv
import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# .envからAPIキーを読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LangChainのLLMインスタンスを作成
llm = ChatOpenAI(openai_api_key=api_key, temperature=0.7, model="gpt-3.5-turbo")

# Streamlitアプリのタイトル
st.title("専門家AIアシスタント")

# 説明文
st.markdown("あなたの質問に、選んだ専門家が答えます。")

# ラジオボタンで専門家を選択
expert = st.radio(
    "相談したい専門家を選んでください：",
    ("医師", "弁護士", "キャリアコンサルタント")
)

# 入力フォーム
user_input = st.text_input("質問を入力してください")

# 送信ボタン
if st.button("送信") and user_input:
    # 専門家に応じたシステムメッセージを作成
    system_prompts = {
        "医師": "あなたは患者に優しく説明する臨床医です。",
        "弁護士": "あなたは法律を簡潔に説明する弁護士です。",
        "キャリアコンサルタント": "あなたは相談者の立場で助言するキャリアコンサルタントです。"
    }

    system_message = SystemMessage(content=system_prompts[expert])
    human_message = HumanMessage(content=user_input)

    with st.spinner("考え中..."):
        response = llm([system_message, human_message])
        st.success("回答:")
        st.write(response.content)

