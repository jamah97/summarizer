

import streamlit as st
from transformers import pipeline

@st.cache(allow_output_mutation=True)

def main():
    sum = pipeline('summarization', device=0)
    text = st.text_input("Text").split()
    st.write(text)
    min = st.select_slider("Pick a min size", 0,300,1)
    max = st.select_slider("Pick a max size", 0,300,1)
    do_sample = st.radio("do_sample", ('False', 'True'))

    if do_sample == 'False':
        st.write(sum(text2, min_length=min, max_length=max, do_sample=False))
    else:
        st.write(sum(text2, min_length=min, max_length=max, do_sample=True))




if __name__ == '__main__':
	main()
