import os
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
import streamlit as st
import streamlit_scrollable_textbox as stx
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

# Set API key for OpenAI Service
os.environ['OPENAI_API_KEY'] = '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'
llm = OpenAI(temperature=0.1, verbose=True)
embeddings = OpenAIEmbeddings()
loader = PyPDFLoader('new1.pdf')
pages = loader.load_and_split()
store = Chroma.from_documents(pages, embeddings, collection_name='new1')
vectorstore_info = VectorStoreInfo(
    name="new1",
    description="Legal documentation PDF",
    vectorstore=store
)
toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)
agent_executor = create_vectorstore_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)
st.set_page_config(page_title="Naydarshan AI", page_icon="⚖️")

st.title("""⚖️ Legal Document Assistant 🏛️""")
st.write(
    """This is a Prototype of Naydarshan AI, a legal document assistant that can help you draft legal documents. To get started, enter a prompt in the 
    text box below and click the "Search" button. You can also view your prompt history in the sidebar.""")


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("Naystyle.css")
prompt = st.text_input('Enter your query here:')
prompt_history = st.session_state.get("prompt_history", [])
search_button = st.button("Search", key="search_button", help="Click to search")
if search_button:

    response = agent_executor.run(prompt)
    st.write("Your Response:", response)
    prompt_history.insert(0, prompt)
    st.session_state.prompt_history = prompt_history
    with st.expander('Document Similarity Search'):
        search = store.similarity_search_with_score(prompt)
        st.write(search[0][0].page_content)

st.sidebar.title("Prompt History")
for i, history_prompt in enumerate(prompt_history, 1):
    st.sidebar.write(f"{i}. {history_prompt}")
