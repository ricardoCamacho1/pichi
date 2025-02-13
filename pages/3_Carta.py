import streamlit as st


if 'unlocked' not in st.session_state or not st.session_state['unlocked']:
    st.error("Debes responder todas las preguntas en la página principal para acceder a esta página.")
    st.stop()

st.set_page_config(page_title="Carta de Amor", page_icon="💌", layout="centered")
st.title("Carta de Amor")

# Open and read the letter text file
with open("assets/carta.txt", "r", encoding="utf-8") as file:
    letter_text = file.read()

# Display the letter text using markdown
st.markdown(letter_text)

st.markdown("---")
st.markdown("<h2 style='text-align: center;'>Video de la Carta</h2>", unsafe_allow_html=True)

# Display the video (ensure the file exists at the specified path)
st.video("assets/videos/carta.mp4")
