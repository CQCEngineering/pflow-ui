import os

import streamlit as st
from dotenv import load_dotenv
import pf


load_dotenv()

endpoint = os.getenv("PROMPTFLOW_ENDPOINT")
api_key = os.getenv("PROMPTFLOW_KEY")
feedback_endpoint = os.getenv("FEEDBACK_ENDPOINT")


result="Waiting for output"

st.image("images/msft_logo.png", width=50) 
st.title("Contoso Chat Assistant")
entity_type = st.text_input("Entity Type")
print(entity_type)
prompt = st.text_input("Input Text")


if st.button("Submit"):
    data = {
        "entity_type": entity_type,
        "text": prompt
    }
    result=pf.process_with_promptflow(data, endpoint, api_key)
    st.text_input("Model Output",value=result,disabled=True)
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:

    st.markdown(f"You selected: {sentiment_mapping[selected]}")
    if selected == 0:
        pf.feedback({"feedback": "thumbsdown"}, api_key,feedback_endpoint)
    else:
        pf.feedback({"feedback": "thumbsup"}, api_key,feedback_endpoint)

