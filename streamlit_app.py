import streamlit as st
from decouple import config
from copythis import CopyThis
import coloredlogs, logging
logger = logging.getLogger(__name__)
coloredlogs.install(level=config('LOG_LEVEL'))

# --------------setup
st.set_page_config(page_title='CopyThis', page_icon='✒️', initial_sidebar_state="auto", menu_items=None)
st.title("CopyThis✒️")
st.text('The day you became a better writer.')
copythis = CopyThis(logger=logger)

input_copy = st.text_area(
    'Paste in Your Copy',
    placeholder='Your copy goes here...', 
    label_visibility="hidden",
    height=300,
)

output_copy = copythis.run(input_copy)

st.caption('The better version is written here 👇🏻')
st.markdown(output_copy)