import streamlit as st
from datetime import datetime

# Configure the page
st.set_page_config(page_title="Contador", page_icon="⏳", layout="centered")

# Page title and description
st.title("⏳ Contador hasta el 15 de Julio de 2025")
st.write("Este contador muestra el tiempo restante en tarjetas para meses, semanas, días, horas y minutos.")

# Define the target date and current date
target_date = datetime(2025, 7, 15)
now = datetime.now()

def create_card(title, value):
    """Returns a card-like HTML string with a white background."""
    card_html = f"""
    <div style="
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px;
        border: 1px solid #ddd;
    ">
        <h3 style="margin-bottom: 5px;">{title}</h3>
        <p style="font-size: 24px; margin: 0;">{value}</p>
    </div>
    """
    return card_html

if target_date > now:
    # Calculate time difference
    time_left = target_date - now
    days = time_left.days
    weeks = days // 7
    hours = days * 24 + time_left.seconds // 3600
    minutes = days * 24 * 60 + time_left.seconds // 60
    # Approximate number of months (using 30 days per month)
    months = days // 30

    # Display the countdown in cards using columns for layout
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(create_card("Meses", months), unsafe_allow_html=True)
    with col2:
        st.markdown(create_card("Semanas", weeks), unsafe_allow_html=True)
    with col3:
        st.markdown(create_card("Días", days), unsafe_allow_html=True)

    col4, col5 = st.columns(2)
    with col4:
        st.markdown(create_card("Horas", hours), unsafe_allow_html=True)
    with col5:
        st.markdown(create_card("Minutos", minutes), unsafe_allow_html=True)
else:
    st.write("La fecha ya ha pasado.")
