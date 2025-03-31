import streamlit as st
import openai
import os
from dotenv import load_dotenv

# 加载本地的 .env 文件，获取 API 密钥
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# 创建 OpenAI 客户端（新版必须这样）
client = openai.OpenAI(api_key=api_key)

st.set_page_config(page_title="AI 问答助手", layout="centered")
st.title("🤖 AI 问答助手")

question = st.text_input("请输入你的问题：")

if st.button("获取回答"):
    if question:
        with st.spinner("AI 思考中..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": question}
                    ],
                    temperature=0.5,
                    max_tokens=512
                )
                answer = response.choices[0].message.content
                st.success("AI 回答：")
                st.write(answer)
            except Exception as e:
                st.error(f"出错啦：{e}")
    else:
        st.warning("请输入问题再点击按钮哦。")
