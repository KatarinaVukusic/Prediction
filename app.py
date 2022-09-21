import streamlit as st
from predict_page import show_predict_page
from visualisation_page import show_visualisation_page
from predict_page import add_bg_from_url


add_bg_from_url() 

page=st.sidebar.selectbox("Explore Or Predict", ("Predict","Explore") )

st.markdown(
    """
<style>
.streamlit-expanderHeader {
    font-size: x-large;
    background-color: #ffff;
}
.streamlit-expanderContent {
  background-color: #ffff;
}


</style>
""",
    unsafe_allow_html=True,
)



if page=="Predict":
    show_predict_page()
else:
    show_visualisation_page()