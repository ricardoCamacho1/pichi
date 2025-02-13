import streamlit as st


if 'unlocked' not in st.session_state or not st.session_state['unlocked']:
    st.error("Debes responder todas las preguntas en la página principal para acceder a esta página.")
    st.stop()
# Set page configuration
st.set_page_config(page_title="Música que Amamos 🎵", page_icon="🎵", layout="centered")

# Page Title and Description
st.title("Música que Amamos")
st.write(
    """
    Aquí encontrarás algunas de las canciones que hemos disfrutado juntos.  
    Selecciona una canción del menú desplegable para reproducirla y revivir esos momentos especiales.  
    ¡Disfruta de la música! 🎶
    """
)

# Dictionary of YouTube videos with their titles as keys and URLs as values.
youtube_videos = {
    "Te Regalo" : "https://youtu.be/39o-RH2OlCU?si=DwaMsVchozUpod2S",
    "Gone Gone Gone": "https://youtu.be/Xc9j9dpj_BQ?si=h5yEbYCKTQJKriCs",
    "Por eso Te Amo": "https://youtu.be/EP8ZYZeUG1k?si=i1wyHwdkkf_qDjhr",
    "Home": "https://youtu.be/lLjvsAyEj-g?si=HlOSrX5POj96ED9y",
    "Make You Feel My Love": "https://youtu.be/EP8ZYZeUG1k?si=i1wyHwdkkf_qDjhr",
    "Blue Jeans": "https://youtu.be/RoLukKZgqkI?si=6LM-aBpwsmjRRq-Q",
    "The Reason": "https://youtu.be/-F9nCQtxkRw?si=36j_Jg3ODoIA8AYw",
    "I Wanna Be Yours": "https://youtu.be/SezFNtFCeQY?si=bi9H66MTe6RlD2Cs",
    "Imagination" : "https://youtu.be/4C7EGz5EwYE?si=3V-NSZNo76uaqATo",
    "We Fell In Love In October" : "https://youtu.be/PDhXVGnSSR8?si=mBZrndFqmuWwFYdg",
    "Apocalypse" : "https://youtu.be/BfU1iB7UBH0?si=DyhOERMqBVW4oMQ0",
    "Un Amor de Verdad" : "https://youtu.be/tsDYGUzQAlw?si=Acf9vjo7Wcle9anI"

}

# Create a dropdown (selectbox) for song selection.
selected_song = st.selectbox("Selecciona una canción", list(youtube_videos.keys()))

# Display the selected video.
if selected_song:
    st.subheader(selected_song)
    st.video(youtube_videos[selected_song])
