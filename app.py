from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import time
load_dotenv()
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-pro')
st.title("GeminiAI")
prompt=st.chat_input("Enter prompt")
try:
    if prompt:
        st.write(prompt)
        with st.spinner("Loading"):
            response = model.generate_content(prompt)
            language = 'en'
            if response.text:
                myobj = gTTS(text=response.text, lang=language, slow=False)  
                myobj.save("response.wav")  
                st.write(response.text)
                st.audio("./response.wav",autoplay=True)
                os.remove("./response.wav")
except:
    st.error("Enter Correct Text")


