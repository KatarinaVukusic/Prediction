
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache
def load_data_for_visualisation():
    df = pd.read_csv("visualisation.csv")
    return df


df = load_data_for_visualisation()


def show_visualisation_page():

    st.title("Visualisation of data")

    st.write("""#### Number of the respondents depending on age""")
    data=df['age'].value_counts()
    st.bar_chart(data)

    st.write("""#### Number of the respondents depending on gender""")
    data=df['sex_male'].value_counts()
    st.bar_chart(data)

    st.write("""#### Number of the respondents depending on glucose levels""")
    data=df['glucose'].value_counts()
    st.bar_chart(data)

    st.write("""#### Number of the respondents depending on total cholesterol levels""")
    data=df['totChol'].value_counts()
    st.bar_chart(data)

    st.write("""#### Risk of CHD based on age""")
    data = df.groupby(["age"])["TenYearCHD"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Risk of CHD based on glucose levels""")
    data = df.groupby(["glucose"])["TenYearCHD"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Risk of CHD based on total cholesterol levels""")
    data = df.groupby(["totChol"])["TenYearCHD"].mean().sort_values(ascending=True)
    st.bar_chart(data)


    st.write("""#### Risk of CHD based on gender""")
    data = df.groupby(["sex_male"])["TenYearCHD"].mean().sort_values(ascending=True)
    st.bar_chart(data)
