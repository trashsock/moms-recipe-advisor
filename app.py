import streamlit as st
from rag_recipes import ask_mom  

st.title("Amma's Recipes")
st.write("What Indian dish are you craving?")

question = st.text_input("Your question:")
if question:
    answer = ask_mom(question)
    st.write(answer)