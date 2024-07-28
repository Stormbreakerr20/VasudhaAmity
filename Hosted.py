import streamlit as st
import streamlit.components.v1 as com
import asyncio
import os

from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)
def response(prompt):
    try:
        completion = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct-v0.3",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=True
        )   
        answer = ""

        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                answer = answer + chunk.choices[0].delta.content
        
        if answer != "":
            return answer
        
        return "No response"
    
    except Exception as e:
        print(e)
        return "No response"

st.set_page_config(page_title="OPDx", page_icon="🩺", layout="wide")


# Get the parent directory
parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
new_parent_directory = os.path.join(os.path.dirname(parent_directory), "app")

# Streamed response emulator
async def response_generator(prompt):
    res = response(prompt)
    return res
        
def colored_markdown(text: str, color: str):
    return f'<p class="title" style="background-color: #fff; color: {color}; padding: 5px; line-height: 1">{text}</p>'

sidebar = st.sidebar
col1, col2 = st.columns([1, 3])

# Display Lottie animation in the first column
with col1:
    com.iframe("https://lottie.host/embed/5899ceed-3498-4546-8ebf-b25561f40002/Xnif8r8nZ4.json", height=400, width=950)

try:
    st.markdown(colored_markdown(f"Virat", "#007bff"),
                unsafe_allow_html=True)  # Blue color
    st.markdown(colored_markdown("How can I help you today ?", "#39A5A9"),
                unsafe_allow_html=True)  # Red color
except:

    st.markdown(colored_markdown(f"Virat", "#007bff"),
                unsafe_allow_html=True)  # Blue color
    st.markdown(colored_markdown("How can I help you today ?", "#39A5A9"),
                unsafe_allow_html=True)  # Red color

st.markdown(
    """
    <style>
        .title {
            text-align: left; 
            font-size: 60px;
            margin-bottom: 0px;
            padding-bottom: 5px;
            display: inline-block;  
        }
        .subtitle {
            text-align: left;
            font-size: 24px;
            color: #333333; 
            margin-top: 5px; 
        }
        .square-container {
            display: flex;
            flex-wrap: wrap;
        }
        .square {
            width: 150px;
            height: 150px;
            background-color: #36A5A9;
            margin: 10px;
            margin-top: 30px;  
            margin-bottom: 50px;  
            color: #ffffff;
            padding: 10px;
            text-align: left;
            font-size: 14px;
            line-height: 1.5;
            border-radius: 16px;
            position: relative;  /* Enable relative positioning for image */
        }
        .square-image {
            position: absolute;  /* Make image absolute within square */
            bottom: 5px;  /* Position image at bottom */
            right: 5px;  /* Position image at right */
            width: 20px;
            height: 20px;
        }
        .input-container {
            display: flex;
            align-items: center;
            position: relative;
            margin-top: 20px;
        }
        .input-text {
            flex: 1;
            height: 40px;
            padding: 10px;
            font-size: 16px;
            border-radius: 12px;
            border: 1px solid #ccc;
            margin-right: 10px;
        }
        .button-container {
            display: flex;
            gap: 0px;
        }
        .button {
            
            height: 40px;
            width: 40px;
            margin: 0px;
            padding: 0px;
            display: flex;
            justify-content: center;
            align-items: center;
            # background-color: #39A5A9;
            color: #fff;
            border-radius: 8px;
            cursor: pointer;
        }
        .button svg {
            width: 24px;
            height: 24px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown(f'<img src="https://i.imgur.com/ngr2HSn.png" width="200">',
                    unsafe_allow_html=True)  # Load image from Imgur with Bitly link

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        generated = asyncio.run(response_generator(prompt))
        response = st.write(generated)
    st.session_state.messages.append({"role": "assistant", "content": generated})

st.sidebar.write("##")
st.sidebar.markdown("<h2 style='text-align: center;'>User Dashboard</h2>", unsafe_allow_html=True)
st.sidebar.write("##")
