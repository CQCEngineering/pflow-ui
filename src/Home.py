import os

import streamlit as st
from dotenv import load_dotenv
import pf


load_dotenv()

endpoint = os.getenv("PROMPTFLOW_ENDPOINT")
api_key = os.getenv("PROMPTFLOW_KEY")
feedback_endpoint = os.getenv("FEEDBACK_ENDPOINT")


result="Waiting for output"
def reset():
    return None #need to do

st.image("images/msft_logo.png", width=50) 
st.title("Contoso Chat Assistant")
entity_type = st.text_input("Entity Type")
print(entity_type)
prompt = st.text_input("Input Text")

st.button("Reset",type="primary", on_click=reset)


if st.button("Submit"):
    data = {entity_type : prompt}
    result=pf.process_with_promptflow(data, endpoint, api_key)
    st.text_input("Model Output",value=result,disabled=True)
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")
    if selected == 0:
        pf.feedback("thumbsdown", api_key,feedback_endpoint)
    else:
        pf.feedback("thumbsup", api_key,feedback_endpoint)


            
#             result = pf.process_with_promptflow(data, promptflow_endpoint, promptflow_key)
            
#             # Display the result from the promptflow processing
#             st.json(result)
# response = f"Echo: {prompt}"
#  Display assistant response in chat message container
# with st.chat_message("assistant"):
#     st.markdown(response)
# Add assistant response to chat history
# st.session_state.messages.append({"role": "assistant", "content": response})



# Add a toggle to select the type of flow
# flow_type = st.radio(
#     "Select the type of flow:",
#     ("Chat", "Document Processing")
# )

#if flow_type == "Chat":
    # Initialize chat history

    
# Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
# # React to user input
# if prompt := st.chat_input("Input Text"):
#     # Display user message in chat message container
#     with st.chat_message("User"):
#         st.markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})  
# response = f"Echo: {prompt}"
# # Display assistant response in chat message container
# with st.chat_message("assistant"):
#     st.markdown(response)
# # Add assistant response to chat history
# st.session_state.messages.append({"role": "assistant", "content": response})


# else:
#     st.subheader("Document Processing")

#     # Input box for pasting text
#     document_text = st.text_area("Paste your document text here:")

#     # Button to submit the text
#     if st.button("Submit"):
#         if document_text:
#             st.write("Document submitted")
#             # Process the document text here
            
#             data = {
#                 "email": document_text
#             }
            
#             result = pf.process_with_promptflow(data, promptflow_endpoint, promptflow_key)
            
#             # Display the result from the promptflow processing
#             st.json(result)
            
#         else:
#             st.write("Please paste some text before submitting.")
            
    