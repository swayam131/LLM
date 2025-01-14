import streamlit as st
import langchain_helper

st.title("Enhancer Generator")

gene = st.sidebar.selectbox("Pick a gene", ("nanog", "sox2", "oct4", "sox9", "pax3"))

if gene:
    response = langchain_helper.generate_assembly_and_enhancers(gene)
    st.header(response['assembly'].strip())
    enhancer = response['enhancers'].strip().split(",")
    st.write("**enhancers**")
    for item in enhancer:
        st.write("-", item)


