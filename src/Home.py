import os

import streamlit as st
from dotenv import load_dotenv

import pf

load_dotenv()

title = os.getenv("TITLE", "Promptflow Test App")
logo_image = os.getenv("LOGO_URL", "images/msft_logo.png")
promptflow_endpoint = os.getenv("PROMPTFLOW_ENDPOINT")
promptflow_key = os.getenv("PROMPTFLOW_KEY")

load_dotenv()


st.image(logo_image, width=50) 
st.title(title)

# Add a toggle to select the type of flow
flow_type = st.radio(
    "Select the type of flow:",
    ("Chat", "Document Processing")
)

if flow_type == "Chat":
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})  
    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


else:
    st.subheader("Document Processing")

    # Input box for pasting text
    document_text = st.text_area("Paste your document text here:")

    # Button to submit the text
    if st.button("Submit"):
        if document_text:
            st.write("Document submitted")
            # Process the document text here
            
            data = {
                "email": document_text
            }
            
            result = pf.process_with_promptflow(data, promptflow_endpoint, promptflow_key)
            
            # Display the result from the promptflow processing
            st.json(result)
            
        else:
            st.write("Please paste some text before submitting.")
            
    