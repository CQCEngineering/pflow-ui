import urllib.request
import json
import streamlit as st



# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script

def process_with_promptflow(data, endpoint, api_key):

    body = str.encode(json.dumps(data))

    # Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint

    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint")


    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(endpoint, body, headers)
    
    with st.spinner("Waiting for response..."):
        try:
            response = urllib.request.urlopen(req)

            result = response.read()
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(error.read().decode("utf8", 'ignore'))
        
    return result
