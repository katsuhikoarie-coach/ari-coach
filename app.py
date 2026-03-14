import streamlit as st
from google import genai
from google.genai import types
from pathlib import Path

# ページ設定
st.set_page_config(
    page_title="ari-coach | メタコーチ Ari 3.0",
    page_icon="🌸",
    layout="centered",
)

# スタイル
st.markdown("""
<style>
    .stChatMessage { font-size: 1.05rem; }
    h1 { text-align: center; }
    .subtitle { text-align: center; color: #888; margin-top: -1rem; margin-bottom: 2rem; }
</style>
""", unsafe_allow_html=True)

st.title("🌸 ari-coach")
st.markdown('<p class="subtitle">メタコーチ Ari 3.0 — 統合的自己変容プロトコル</p>', unsafe_allow_html=True)

# APIキー設定（Streamlit Cloud は secrets、ローカルは .env）
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    import os
    from dotenv import load_dotenv
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY が設定されていません。")
    st.stop()

# Geminiクライアント初期化
@st.cache_resource
def get_client(key):
    return genai.Client(api_key=key)

client = get_client(api_key)

# 利用可能なモデルを自動選択
@st.cache_resource
def get_model_name(_client):
    preferred = [
        "gemini-2.5-pro",
        "gemini-2.5-flash",
        "gemini-2.0-flash",
        "gemini-2.0-flash-lite",
        "gemini-1.5-flash",
    ]
    try:
        available = {m.name.replace("models/", "") for m in _client.models.list()}
        for m in preferred:
            if m in available:
                return m
    except Exception:
        pass
    return preferred[0]

model_name = get_model_name(client)

# システムプロンプト読み込み
@st.cache_resource
def load_system_prompt():
    prompt_path = Path(__file__).parent / "最強セルフコーチング_プロンプト_3.0.md"
    return prompt_path.read_text(encoding="utf-8")

system_prompt = load_system_prompt()

# セッション状態の初期化
if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(
        model=model_name,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
        ),
    )
    st.session_state.messages = []
    with st.spinner("Ariが準備中..."):
        opening = st.session_state.chat.send_message(
            "セッションを開始してください。Phase 0の最初の一問だけを置いてください。"
        )
        st.session_state.messages.append({
            "role": "assistant",
            "content": opening.text
        })

# 会話履歴の表示
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ユーザー入力
if user_input := st.chat_input("ここに入力してください..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner(""):
            response = st.session_state.chat.send_message(user_input)
            reply = response.text
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})

# サイドバー：リセットボタン
with st.sidebar:
    st.markdown("### セッション管理")
    if st.button("🔄 新しいセッションを開始", use_container_width=True):
        del st.session_state["chat"]
        del st.session_state["messages"]
        st.rerun()
    st.markdown("---")
    st.markdown("**ari-coach** は、アドラー心理学・CBT・ACT・IFSなど13の心理・コーチング手法を統合したAIコーチです。")
