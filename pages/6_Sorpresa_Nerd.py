import streamlit as st
import numpy as np
import math
import plotly.graph_objects as go


if 'unlocked' not in st.session_state or not st.session_state['unlocked']:
    st.error("Debes responder todas las preguntas en la página principal para acceder a esta página.")
    st.stop()

    
st.set_page_config(page_title="Regalos 3D: Corazón y Rosa", page_icon="❤️🌹", layout="centered")
st.title("Formas 3D: Corazón y Rosa")
st.write("Selecciona que quieres ver ajusta los parámetros para modificarlos.")

# Dropdown to select between the two forms.
form_option = st.selectbox("Selecciona la forma", ["Corazón", "Rosa"])

if form_option == "Corazón":
    st.header("❤️ Corazón 3D ❤️")
    st.write("Mi niña hermosa, aqui tienes mi corazon, es un arepresentación de que mi corazón es tuyo y puedes hacer lo que quieras con el.")
    # Sliders for the heart
    scale_x = st.slider("Anchura", min_value=0.5, max_value=3.0, value=1.0, step=0.1)
    scale_y = st.slider("Profundidad", min_value=0.5, max_value=3.0, value=1.0, step=0.1)
    scale_z = st.slider("Altura", min_value=0.5, max_value=3.0, value=1.0, step=0.1)
    resolution = st.slider("Resolución", min_value=30, max_value=100, value=50, step=5)
    
    # Create a 3D grid of points.
    x = np.linspace(-1.5 * scale_x, 1.5 * scale_x, resolution)
    y = np.linspace(-1.5 * scale_y, 1.5 * scale_y, resolution)
    z = np.linspace(-1.5 * scale_z, 1.5 * scale_z, resolution)
    X, Y, Z = np.meshgrid(x, y, z)

    # Define the heart equation.
    # ((x)^2 + (9/4)*(y)^2 + (z)^2 - 1)^3 - (x)^2*(z)^3 - (9/80)*(y)^2*(z)^3 = 0
    F = (((X / scale_x) ** 2 + (9/4) * (Y / scale_y) ** 2 + (Z / scale_z) ** 2 - 1) ** 3 -
         (X / scale_x) ** 2 * (Z / scale_z) ** 3 -
         (9/80) * (Y / scale_y) ** 2 * (Z / scale_z) ** 3)

    # Create an isosurface plot for the heart.
    fig = go.Figure(data=go.Isosurface(
        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),
        value=F.flatten(),
        isomin=0,
        isomax=0,
        surface_count=1,
        colorscale='Reds',
        caps=dict(x_show=False, y_show=False, z_show=False)
    ))
    fig.update_layout(
        title="Corazón 3D",
        scene=dict(aspectmode="data"),
        margin=dict(l=0, r=0, t=40, b=0)
    )
    st.plotly_chart(fig, use_container_width=True)

elif form_option == "Rosa":
    st.header("🌹 Rosa 3D 🌹")
    st.write("Esto es un a rosa, y es la segunda rosa eterna que te regalo, la primera es el peluchin :)")
    # Sliders for the rose – these mirror the p5.js parameters.
    opening   = st.slider("Apertura de la Rosa", min_value=1.0, max_value=10.0, value=2.0, step=0.1)
    vDensity  = st.slider("Densidad Vertical", min_value=1.0, max_value=20.0, value=8.0, step=0.1)
    pAlign    = st.slider("Alineación de los Pétalos", min_value=0.0, max_value=6.0, value=3.6, step=0.05)
    curve1    = st.slider("Curvatura 1", min_value=-6.0, max_value=6.0, value=2.0, step=0.1)
    curve2    = st.slider("Curvatura 2", min_value=0.5, max_value=1.5, value=1.3, step=0.1)
    
    # Use a fixed grid for the rose.
    cols = 100  # (originally 600 in the p5.js code; reduced here for performance)
    rows = 30
    t_D = (180 * 15) / cols  # Angle increment in degrees.
    r_D = 1 / rows           # Normalized radial step.
    
    vertices = []  # To store (x, y, z) for each vertex.
    
    # Loop over the grid to calculate vertex positions.
    for r in range(rows + 1):
        r_norm = r * r_D
        for theta in range(cols + 1):
            theta_deg = theta * t_D
            theta_rad = math.radians(theta_deg)
            # Compute phi in degrees, then convert to radians.
            phi_deg = (180 / opening) * math.exp(-theta * t_D / (vDensity * 180))
            phi_rad = math.radians(phi_deg)
            
            # Compute petalCut using the pAlign parameter.
            pAlignTerm = ((pAlign * theta * t_D) % 360) / 180.0
            petalCut = 1 - 0.5 * (((5/4) * ((1 - pAlignTerm)**2) - 1/4)**2)
            
            # Compute hangDown using curve1 and curve2.
            hangDown = curve1 * (r_norm ** 2) * ((curve2 * r_norm - 1) ** 2) * math.sin(phi_rad)
            
            # Calculate the vertex position.
            factor = 260 * petalCut
            pX = factor * (r_norm * math.sin(phi_rad) + hangDown * math.cos(phi_rad)) * math.sin(theta_rad)
            pY = -factor * (r_norm * math.cos(phi_rad) - hangDown * math.sin(phi_rad))
            pZ = factor * (r_norm * math.sin(phi_rad) + hangDown * math.cos(phi_rad)) * math.cos(theta_rad)
            
            vertices.append((pX, pY, pZ))
    
    # Prepare lists of coordinates.
    x_vals = [v[0] for v in vertices]
    y_vals = [v[1] for v in vertices]
    z_vals = [v[2] for v in vertices]
    
    # Build triangle indices from the grid.
    i_indices = []
    j_indices = []
    k_indices = []
    for r in range(rows):
        for theta in range(cols):
            idx = r * (cols + 1) + theta
            idx_right = idx + 1
            idx_down = idx + (cols + 1)
            idx_down_right = idx_down + 1
            
            # First triangle of the quad.
            i_indices.append(idx)
            j_indices.append(idx_down)
            k_indices.append(idx_down_right)
            # Second triangle of the quad.
            i_indices.append(idx)
            j_indices.append(idx_down_right)
            k_indices.append(idx_right)
    
    # Create a Plotly Mesh3d object for the rose.
    fig = go.Figure(data=go.Mesh3d(
        x=x_vals,
        y=y_vals,
        z=z_vals,
        i=i_indices,
        j=j_indices,
        k=k_indices,
        color='crimson',
        opacity=0.8,
        flatshading=True,
        colorscale='Reds'
    ))
    fig.update_layout(
        title="Rosa 3D",
        scene=dict(aspectmode="data"),
        margin=dict(l=0, r=0, t=40, b=0)
    )
    st.plotly_chart(fig, use_container_width=True)
