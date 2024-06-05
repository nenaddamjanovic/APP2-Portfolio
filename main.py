import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Nenad Damjanović")
    content = """ I hold a Bachelor of Computer Science degree, with over a decade of seasoned expertise in IT system administration and
networking. As a team player, I thrive in team settings, known for my ability to tackle new challenges head-on and learn on the
fly. I am deeply committed to my work and continuously seek opportunities for improvement. My aspiration is to contribute
my skills and enthusiasm in large organizations with extensive workforces. In my next role, I aim to leverage my expertise in
networking and IT in general, while also expanding my proficiency in Python programming and other programming languages. """
    # st.write(content)
    st.info(content)