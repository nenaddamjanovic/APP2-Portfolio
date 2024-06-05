import streamlit as st
import pandas

st.set_page_config(layout="wide")

# col1, col2 = st.columns(2)
col1, empty_col, col2 = st.columns([1.5, 0.5, 2.5])

with col1:
    st.image("images/photo.jpg")  # jazavicar
    # st.image("images/photo.png")  # Nenad

with col2:
    st.title("Nenad Damjanović")
    content = """
I hold a Bachelor of Computer Science degree, with over a decade of seasoned expertise in IT system administration and
networking. As a team player, I thrive in team settings, known for my ability to tackle new challenges head-on and learn on the
fly. I am deeply committed to my work and continuously seek opportunities for improvement. My aspiration is to contribute
my skills and enthusiasm in large organizations with extensive workforces. In my next role, I aim to leverage my expertise in
networking and IT in general, while also expanding my proficiency in Python programming and other programming languages. 
"""
    # st.write(content)
    st.info(content)

st.divider()
content2 = """
Python programming (Django, Flask, GeoPython, PyGame)
"""
st.write(content2)
st.divider()

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")  #  Učitavamo csv fajl

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
