import streamlit as st
import os
from PIL import Image, ImageOps


if 'unlocked' not in st.session_state or not st.session_state['unlocked']:
    st.error("Debes responder todas las preguntas en la página principal para acceder a esta página.")
    st.stop()


# Configure the page
st.set_page_config(page_title="Cápsula del Tiempo", page_icon="⏳", layout="centered")

# Page title and description
st.title("⏳ Cápsula del Tiempo ⏳")
st.write(
    """
    En esta página hay una pizca de todo lo que hemos pasado juntos, momentos felices. 😻

    Cada foto representa un momento muy especial en mi vida, de los mejores, y espero lo disfrutes y sientas 
    tan bonito al ver todos estos instantes tanto como yo. Te amo ! 💕❤️
    """
)

# Path to the folder containing our photos
photos_folder = "assets/photos"

# Dynamically list image files in the folder (filter by common image extensions)
try:
    image_files = [
        os.path.join(photos_folder, f)
        for f in os.listdir(photos_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ]
except Exception as e:
    st.error("No se pudo acceder a las fotos. Verifica la ruta y los permisos.")
    image_files = []

# Check if there are any images and display them in a grid layout
if image_files:
    # Define the number of columns for the grid
    num_cols = 3
    # Sort the files if you wish (e.g., alphabetically or by date)
    image_files.sort()
    
    # Display images in rows with 'num_cols' columns each
    for i in range(0, len(image_files), num_cols):
        cols = st.columns(num_cols)
        for idx, file in enumerate(image_files[i:i+num_cols]):
            with cols[idx]:
                # Open the image and apply EXIF orientation if necessary
                image = Image.open(file)
                image = ImageOps.exif_transpose(image)
                st.image(image, use_container_width=True)
else:
    st.write("No hay fotos disponibles en este momento. ¡Agrega algunos recuerdos a la carpeta 'assets/photos'!")
