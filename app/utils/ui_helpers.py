import streamlit as st
import base64
import os


def set_bg(overlay_color="rgba(255,255,255,0.5)"):
    """
    Sets a background image (and optional color overlay) for all Streamlit pages.
    """


    current_dir = os.path.dirname(__file__)

    # Go one level up from utils → app, then into assets/
    image_path = os.path.join(current_dir, "..", "assets", "background.jpg")
    image_path = os.path.abspath(image_path)


    # Read and encode image
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    # --- Background image ---
    bg_css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"], [data-testid="stSidebar"] {{
        background: rgba(255,255,255,0.5);
        backdrop-filter: blur(4px);
    }}
    [data-testid="stAppViewContainer"]::before {{
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: {overlay_color};
        z-index: 0;
    }}
    [data-testid="stAppViewContainer"] > div {{
        position: relative;
        z-index: 1;
    }}
    </style>
    """
    st.markdown(bg_css, unsafe_allow_html=True)
