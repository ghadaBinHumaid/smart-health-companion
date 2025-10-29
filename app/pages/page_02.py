import streamlit as st
import requests
from utils.ui_helpers import set_bg

set_bg()

if st.button("⬅️ Return to Main Page"):
    st.switch_page("app.py")

st.title("🧠 Diagnosis Assistant")

st.write("Describe your symptoms below, and the model will predict the likely disease.")

# --- Input form ---
with st.form("diagnosis_form"):
    st.subheader("🩺 What symptoms do you have?")
    text = st.text_area(
        "List your symptoms (e.g., fatigue, hair loss, weight gain, joint pain)",
        height=150,
        placeholder="Type your symptoms here..."
    )
    submitted = st.form_submit_button("🔍 Diagnose")

# --- Run only when the form is submitted ---
if submitted:
    if not text.strip():
        st.warning("⚠️ Please enter your symptoms before diagnosing.")
    else:
        st.info("⏳ Analyzing symptoms and predicting the likely disease...")

        url = "https://remedyrecommenderimage-745821369635.europe-west1.run.app/predict_disease"

        params = {"symptoms_text": text}
        resp = requests.get(url, params=params, timeout=15)


        data = resp.json()
        disease = data.get("disease")

        if disease:
            st.success("✅ The most likely disease is:")
            html = f"""
                <div style="
                    background-color: #f9f9f9;
                    border-left: 6px solid #4CAF50;
                    border-radius: 10px;
                    padding: 12px 16px;
                    margin-bottom: 10px;
                    box-shadow: 0px 2px 6px rgba(0,0,0,1);
                ">
            <div style="display:flex;align-items:center;gap:10px;color:#1b5e20;">
                <span style="font-size:20px;">🩺</span>
                <span style="font-weight:700;font-size:18px;">The most likely disease</span>
            </div>
            <div style="margin: 4px 0;color:#000000;"><b>{disease}</b></div>
            </div>
            """
            st.markdown(html, unsafe_allow_html=True)

        else:
            st.warning("No 'disease' field found in the API response. Please verify the backend output.")
