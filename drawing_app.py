import streamlit as st
from PIL import Image, ImageDraw
import numpy as np

st.title("🎨 Simple Logo / Doodle Designer")

# Canvas size
width, height = 600, 400

# Create blank canvas
if "canvas" not in st.session_state:
    st.session_state.canvas = Image.new("RGB", (width, height), "white")
    st.session_state.draw = ImageDraw.Draw(st.session_state.canvas)

# Color & brush size
color = st.color_picker("Pick a color", "#000000")
brush_size = st.slider("Brush size", 1, 20, 3)

# Draw on canvas with mouse drag simulation (click-based)
x = st.number_input("X coordinate", min_value=0, max_value=width, value=100)
y = st.number_input("Y coordinate", min_value=0, max_value=height, value=100)

if st.button("Draw Point"):
    st.session_state.draw.ellipse(
        [x-brush_size, y-brush_size, x+brush_size, y+brush_size],
        fill=color,
        outline=color
    )

st.image(st.session_state.canvas)

if st.button("Clear Canvas"):
    st.session_state.canvas = Image.new("RGB", (width, height), "white")
    st.session_state.draw = ImageDraw.Draw(st.session_state.canvas)