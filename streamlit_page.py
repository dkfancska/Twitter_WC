import urllib
from datetime import time
import time as tm
import streamlit as st
from PIL import Image
import wc
import re



OCTOPUS_ICON = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/apple/285/jack-o-lantern_1f383.png"
st.set_page_config(page_title="Twitter WC", page_icon=OCTOPUS_ICON)

st.image(OCTOPUS_ICON, width=100)
st.title("Make your twitter world cloud ✨")
username = st.text_input("Your twitter username")
clicked = st.button("Show preview")
qq = st.empty()
title_container = st.container()
checkboxes_external = st.container()
wc_image = st.container()

if clicked:
    title_container = st.empty()
    if len(username) >= 1:

        with qq:
            st.write('Getting result. Wait some seconds')

        st.empty()
        with title_container:
            st.empty()

        with title_container:
            try:
                path = wc.rr(username)
                image = Image.open(path)
                st.image(image)
                wc.rm_file(path)
                with qq:
                    st.write('Your result')
            except:

                st.error('Error! User Not Found!')
        st.write("---")

    else:

        with qq:
            st.error('Enter your username')
