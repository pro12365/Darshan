import streamlit as st
import streamlit_scrollable_textbox as stx

st.set_page_config(page_title="Naydarshan AI", page_icon="📄")

st.title('👩🏻‍⚖️🏛️⚖ Legal Document Assistant')
st.write('This is a Prototype of Naydarshan AI, a legal document assistant that can help you draft legal documents. It is powered by GPT-3, a state-of-the-art language model developed by OpenAI. To get started, enter a prompt in the text box below and click the "Search" button. You can also view your prompt history in the sidebar.')

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("Naystyle.css")
prompt = st.text_input('Enter your query here:')
prompt_history = st.session_state.get("prompt_history", [])
search_button = st.button("Search", key="search_button", help="Click to search")

if search_button:
    st.write("Searching for:", prompt)
    prompt_history.insert(0, prompt)  # Insert the current prompt at the beginning
    st.session_state.prompt_history = prompt_history  # Store the updated history in session state

st.sidebar.title("Prompt History")
for i, history_prompt in enumerate(prompt_history, 1):
    st.sidebar.write(f"{i}. {history_prompt}")

stx.scrollableTextbox('Here will be the Generated output...')

