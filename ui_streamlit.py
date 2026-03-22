import json
import os
import requests
import streamlit as st

# -----------------------------
# Config
# -----------------------------
DEFAULT_API_BASE = os.getenv("API_BASE_URL", "http://localhost:8000")

st.set_page_config(
    page_title="Enterprise RAG Agents (Gemini) — UI",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Enterprise Document Q & A (Gemini + RAG + Agents)")
st.caption(
    "Upload enterprise documents, then ask questions. Answers are grounded in retrieved context and verified by a verifier agent."
)

# Sidebar settings
with st.sidebar:
    st.header("Settings")
    api_base = st.text_input(
        "FastAPI Base URL",
        value=DEFAULT_API_BASE,
        help="Example: http://localhost:8000",
    )
    st.divider()
    st.markdown("**Flow**: Upload → Index → Ask → (Answer + Verification)")

# Session state
if "chat" not in st.session_state:
    st.session_state.chat = (
        []
    )  # list of dicts: {"role": "user/assistant", "content": "..."}
if "last_upload" not in st.session_state:
    st.session_state.last_upload = None


# -----------------------------
# Helpers
# -----------------------------
def api_post_file(endpoint: str, file):
    url = f"{api_base.rstrip('/')}{endpoint}"
    files = {"file": (file.name, file.getvalue(), file.type)}
    r = requests.post(url, files=files, timeout=300)
    return r


def api_post_json(endpoint: str, payload: dict):
    url = f"{api_base.rstrip('/')}{endpoint}"
    r = requests.post(url, json=payload, timeout=300)
    return r


# -----------------------------
# Layout: Upload + Ask
# -----------------------------
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.subheader("1) Upload documents")
    st.write("Supported: PDF, TXT, CSV, XLSX/XLS")

    uploaded_files = st.file_uploader(
        "Choose one or more files",
        type=["pdf", "txt", "csv", "xlsx", "xls"],
        accept_multiple_files=True,
    )

    if st.button(
        "Upload & Index",
        type="primary",
        use_container_width=True,
        disabled=not uploaded_files,
    ):
        results = []
        with st.spinner("Uploading and indexing..."):
            for f in uploaded_files:
                try:
                    resp = api_post_file("/upload", f)
                    if resp.status_code == 200:
                        results.append(resp.json())
                    else:
                        results.append({"file": f.name, "error": resp.text})
                except Exception as e:
                    results.append({"file": f.name, "error": str(e)})

        st.session_state.last_upload = results
        st.success("Done.")

    if st.session_state.last_upload:
        st.subheader("Upload results")
        st.json(st.session_state.last_upload)

with col2:
    st.subheader("2) Ask questions")
    question = st.text_area(
        "Enter your question",
        placeholder="Example: What is the payment approval policy in the finance document?",
        height=90,
    )

    ask_col_a, ask_col_b = st.columns([1, 1])
    with ask_col_a:
        ask_btn = st.button(
            "Ask",
            type="primary",
            use_container_width=True,
            disabled=not question.strip(),
        )
    with ask_col_b:
        clear_btn = st.button("Clear chat", use_container_width=True)

    if clear_btn:
        st.session_state.chat = []
        st.rerun()

    if ask_btn:
        st.session_state.chat.append({"role": "user", "content": question})

        with st.spinner("Thinking (Gemini + RAG + Agents)..."):
            try:
                resp = api_post_json("/ask", {"question": question})
                if resp.status_code != 200:
                    answer_text = f"API error {resp.status_code}: {resp.text}"
                    verification_text = ""
                else:
                    data = resp.json()
                    answer_text = data.get("answer", "")
                    verification_text = data.get("verification", "")

                st.session_state.chat.append(
                    {"role": "assistant", "content": answer_text}
                )
                # store verifier separately for display
                st.session_state.chat.append(
                    {"role": "verifier", "content": verification_text}
                )

            except Exception as e:
                st.session_state.chat.append(
                    {"role": "assistant", "content": f"Request failed: {e}"}
                )

        st.rerun()


# -----------------------------
# Chat display
# -----------------------------
st.divider()
st.subheader("Conversation")

for msg in st.session_state.chat:
    role = msg["role"]
    content = msg["content"]

    if role == "user":
        with st.chat_message("user"):
            st.markdown(content)

    elif role == "assistant":
        with st.chat_message("assistant"):
            st.markdown(content)

    elif role == "verifier":
        with st.expander("Verifier output (JSON)", expanded=False):
            # Try pretty JSON, else raw text
            try:
                parsed = json.loads(content)
                st.json(parsed)
            except Exception:
                st.code(content or "(empty)")
