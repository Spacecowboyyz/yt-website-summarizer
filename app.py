import streamlit as st
import validators
from langchain_classic.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader


st.set_page_config(page_title="Langchain : Summarize Text From YT or Website",page_icon="🦜")
st.title("🦜 Langchain : Summarize Text From YT or Website")
st.subheader('Summarize URL')

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key",value="",type="password")

generic_url = st.text_input("URL",label_visibility="collapsed")

llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=groq_api_key)

prompt_template = """
Provide a summary of the following content in 300 words:
content : {text}
"""
prompt = PromptTemplate(template = prompt_template,input_variables = ['text'])

with st.sidebar:
    groq_api_key = st.text_input("Groq API Key",value="",type="password")
generic_url = st.text_input("URL",label_visibility="collapsed")

prompt_template = """
Provide a summary of the following content in 300 words:
content : {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=['text'])

if st.button("Summarize the content from YT or Website"):
    if not groq_api_key.strip():
        st.error("Please provide the GROQ API KEY to get started...")
    elif not generic_url.strip():
        st.error("Please provide the essential url for further summarization...")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It may be a YT video URL or Website URL...")
    else:
        try:
            llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=groq_api_key)  # ✅ ab yahan, key mil chuki hogi
            with st.spinner("Waiting...."):
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=True,
                        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
                    )
                docs = loader.load()
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                st.write(f"Docs loaded: {len(docs)}")
                if docs:
                    st.write(f"Content length: {len(docs[0].page_content)}")
                    st.write(docs[0].page_content[:300])
                output_summary = chain.run(docs)
                st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception:{e}")

                    
