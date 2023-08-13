import streamlit as st
from decouple import config
import coloredlogs, logging
logger = logging.getLogger(__name__)
coloredlogs.install(level=config('LOG_LEVEL', default='INFO'))
from dotenv import find_dotenv, load_dotenv
import os

# --------------setup
st.set_page_config(page_title='CopyThis', page_icon='✒️', initial_sidebar_state="auto", menu_items=None)
st.title("CopyThis✒️")
st.text('The day you became a better writer.')

st.sidebar.subheader("Enter Your API Key 🗝️")
open_api_key = st.sidebar.text_input(
    "Open API Key", 
    value=st.session_state.get('open_api_key', ''),
    help="Get your API key from https://openai.com/",
    type='password'
)
os.environ["OPENAI_API_KEY"] = open_api_key
st.session_state['open_api_key'] = open_api_key
load_dotenv(find_dotenv())

from copythis import CopyThis
copythis = CopyThis(logger=logger)

@st.cache_data
def improve_copy(input_copy):
    return copythis.run(input_copy)

input_copy = st.text_area(
    'Paste in Your Copy',
    placeholder='Your copy goes here...', 
    label_visibility="hidden",
    height=300,
)

if input_copy != "" and (open_api_key == '' or open_api_key is None):
    st.error("⚠️ Please enter your API key in the sidebar")

st.caption('The better version is written here 👇🏻')


if input_copy != '' and input_copy != 'Your copy goes here...':
    output_copy, final_prompt = improve_copy(input_copy)
    st.markdown(output_copy)

    with st.expander("Show Final Prompt"):
        st.markdown(final_prompt)