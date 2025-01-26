# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token


import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "b60eb861-1b0a-4210-a15a-3aa3e87fdc2a"
FLOW_ID = "8dd914d6-e9a1-4227-9081-fc3a24256cf2"
APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "Customer" # The endpoint name of the flow


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Chat Interface")

    message = st.text_area("Message", placeholder="Ask something...")

    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message")
            return
        
        try:
            with st.spinner("Running flow..."):
                response = run_flow(message)

            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()

# results = run_flow("what are the shipment times")
# print(results)


# # test code for api call

# import requests
# from dotenv import load_dotenv
# import os
# import traceback

# load_dotenv()

# BASE_API_URL = "https://api.langflow.astra.datastax.com"
# LANGFLOW_ID = "b60eb861-1b0a-4210-a15a-3aa3e87fdc2a"
# FLOW_ID = "8dd914d6-e9a1-4227-9081-fc3a24256cf2"
# APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
# ENDPOINT = "Customer"

# def run_flow(message: str) -> dict:
#     api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
#     payload = {
#         "input_value": message,
#         "output_type": "chat",
#         "input_type": "chat",
#     }
#     headers = {
#         "Authorization": "Bearer " + APPLICATION_TOKEN, 
#         "Content-Type": "application/json"
#     }
    
#     try:
#         response = requests.post(api_url, json=payload, headers=headers)
        
#         # Print raw response for debugging
#         print("Response Status Code:", response.status_code)
#         print("Response Headers:", response.headers)
#         print("Response Text:", response.text)
        
#         # Add more robust error checking
#         response.raise_for_status()
        
#         return response.json()
    
#     except requests.exceptions.RequestException as e:
#         print(f"Request Error: {e}")
#         print(traceback.format_exc())
#         return None
#     except ValueError as e:
#         print(f"JSON Decode Error: {e}")
#         print(traceback.format_exc())
#         return None

# # Test the function
# results = run_flow("what are the shipment times")
# print(results)