import os
import pf
from dotenv import load_dotenv

load_dotenv()




promptflow_endpoint = os.getenv("PROMPTFLOW_ENDPOINT")
promptflow_key = os.getenv("PROMPTFLOW_KEY")



data = {
    "email": "Where can I find info on foodbanks?"
}

pf.process_with_promptflow(data, promptflow_endpoint, promptflow_key)
    

