import streamlit as st
import os

from utils import * #importing all functions from utils.py


def main():
    st.set_page_config(page_title="PDF Summarization Tool")
    
    
    
    st.title("PDF Summarizing App")
    st.write("summarize your pdf files in just a few seconds.")
    st.write("Developed by Aayush Meel")
    st.divider()
    
    
    
    pdf=st.file_uploader("Upload your PDF file", type="pdf")
    
    submit=st.button("Generate Summary")
    os.environ["OPENAI_API_KEY"]="Enter your OpenAI API Key"   #Get an OpenAI API and paste it here 
    if submit:
        response=summarizer(pdf)
        
        
        st.subheader("Summary of File:")
        st.write(response)
    
if __name__ == "__main__":
    main()
