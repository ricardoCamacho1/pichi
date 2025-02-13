import streamlit as st
import time
import datetime
from PIL import Image, ImageOps

# Set page configuration
st.set_page_config(page_title="Mi Propuesta 💖", page_icon="💌", layout="centered")

# Initialize session state variables if not present.
if 'unlocked' not in st.session_state:
    st.session_state['unlocked'] = False
if 'question_index' not in st.session_state:
    st.session_state['question_index'] = 0

# Define the list of unlock questions.
questions = [
    {
        "question": "Cual es tu nickname?",
        "input_type": "text",
        "correct": lambda ans: ans.strip().lower() == "pichi",
        "image": "assets/photos/pichi.jpeg"
    },
    {
        "question": "Cuando fue la primera vez que te pedi?",
        "input_type": "date",
        "correct": lambda ans: ans == datetime.date(2022, 10, 8),
        "image": "assets/photos/mochomos.jpeg"
    },
    {
        "question": "Cuando fue la ultima vez que te pedi?",
        "input_type": "date",
        "correct": lambda ans: ans == datetime.date(2025, 1, 11),
        "image": "assets/photos/picnic.jpeg"
    },
    {
        "question": "A que cafe fuimos con regi y Raquel?",
        "input_type": "text",
        "correct": lambda ans: ans.strip().lower() == "hello kitty",
        "image": "assets/photos/coffee.jpeg"
    },
    {
        "question": "Cual fue el primer ramo de flores que te di?",
        "input_type": "text",
        "correct": lambda ans: "girasol" in ans.strip().lower() and "rosas rojas" in ans.strip().lower(),
        "image": "assets/photos/ramo.jpeg"
    },
    {
        "question": "Donde fue Nuestra primer chocoaventura? (Hint: Hot dogs Picosos y pichi cansada)",
        "input_type": "text",
        "correct": lambda ans: ans.strip().lower() == "fundidora",
        "image": "assets/photos/fundidora.jpeg"
    },
    {
        "question": "Quien es la mujer mas guapa, chingona, inteligente, sexy, preciosa, hermosa, maravillosa, perfecta...?",
        "input_type": "text",
        "correct": lambda ans: ans.strip().lower() in ["pichi", "michi", "mich", "yo"],
        "image": "assets/photos/michi.jpeg"
    }
]

# ------------------ UNLOCK QUIZ ------------------ #
if not st.session_state['unlocked']:
    st.header("Desbloquea la app respondiendo las siguientes preguntas:")
    current_index = st.session_state['question_index']
    if current_index < len(questions):
        current_q = questions[current_index]
        st.subheader(f"Pregunta {current_index + 1} de {len(questions)}")
        st.write(current_q["question"])
        
        # Use the appropriate input widget.
        if current_q["input_type"] == "text":
            answer = st.text_input("Tu respuesta:")
        elif current_q["input_type"] == "date":
            answer = st.date_input("Selecciona la fecha:")
        
        if st.button("Enviar respuesta"):
            if current_q["correct"](answer):
                st.success("¡Correcto!")
                st.balloons()
                # Open and display the image with proper orientation.
                img = Image.open(current_q["image"])
                img = ImageOps.exif_transpose(img)
                st.image(img, use_container_width=True)
                st.session_state['question_index'] = current_index + 1
                time.sleep(3)
                st.rerun()
            else:
                st.error("Incorrecto, intenta de nuevo.")
    else:
        st.session_state['unlocked'] = True
        st.success("¡Todas las respuestas son correctas! Bienvenida a la app.")
        st.balloons()
        time.sleep(3)
        st.rerun()

# ------------------ MAIN PROPOSAL CONTENT ------------------ #
else:
    # Custom styles.
    st.markdown(
        """
        <style>
        .big-font {
            font-size:40px !important;
            text-align: center;
            color: #FF4081;
        }
        .success-box {
            background-color: #d4edda;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: #155724;
            margin: auto;
            width: 70%;
        }
        .stButton>button {
            font-size: 24px !important;
            padding: 15px 30px !important;
            width: 100% !important;
            border-radius: 10px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Display the Valentine's message.
    st.markdown('<p class="big-font">¿Quieres ser mi Valentín? 💖</p>', unsafe_allow_html=True)
    
    # Button options with bigger size.
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.button("Tal vez 🤔", disabled=True)
    with col2:
        yes_clicked = st.button("Sí 💘")
    with col3:
        st.button("No 💔", disabled=True)
    
    # If "Sí" is clicked, show celebration, success message, video sections and images.
    if yes_clicked:
        st.balloons()
        st.markdown(
            '<div class="success-box">'
            '¡Sabía que dirías que sí! 🎉💖<br><br>'
            'Te amo mucho mucho mucho 😘<br><br>'
            'Hice todo esto para ti, explora la app para descubrir más sorpresas. 💝'
            '</div>',
            unsafe_allow_html=True
        )
        time.sleep(1.5)
        st.snow()
        
        st.markdown("---")
        st.markdown('<p class="big-font">💝 Un video especial para ti 💝</p>', unsafe_allow_html=True)
        
        # First Video (Bobba)
        st.markdown("<p class='big-font'>Bobba</p>", unsafe_allow_html=True)
        st.markdown("Hice el video con AI inspirado en Tapioca de Milk Tea, un drink que amamos.")
        st.video("assets/videos/bobba.mp4")
        
        st.markdown("---")
        
        # Second Video (Chofi)
        st.markdown("<p class='big-font'>Chofi</p>", unsafe_allow_html=True)
        st.markdown("Hice el video con AI inspirado en Chofi, con su peluche de tortuga.")
        st.video("assets/videos/chofi.mp4")
        
        # Display the images corresponding to each quiz question.
        st.markdown("---")
        st.markdown('<p class="big-font">Recuerda estos momentos:</p>', unsafe_allow_html=True)
        
        # We'll show images in rows with up to 3 columns per row.
        num_cols = 3
        num_questions = len(questions)
        rows_needed = (num_questions + num_cols - 1) // num_cols
        
        for i in range(rows_needed):
            cols = st.columns(num_cols)
            for j in range(num_cols):
                idx = i * num_cols + j
                if idx < num_questions:
                    with cols[j]:
                        img = Image.open(questions[idx]["image"])
                        img = ImageOps.exif_transpose(img)
                        st.image(img, use_container_width=True)
