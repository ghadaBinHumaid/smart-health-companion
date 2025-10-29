import streamlit as st
import requests
import pandas as pd
from utils.ui_helpers import set_bg



set_bg()

if st.button("⬅️ Return to Main Page"):
    st.switch_page("app.py")

st.title("🩺 Remedy Recommendation ")

st.write("Provide your disease and get remedy suggestions:")

DISEASES = [
    "Hashimoto's Thyroiditis", "Celiac", "Chronic Fatigue Syndrome", "Fibromyalgia",
    "Crohn's Disease", "Long COVID", "Ulcerative Colitis", "Lupus",
    "Multiple Sclerosis", "Type 1 Diabetes"
]

with st.form("assessment_form"):
    st.subheader("1) What disease do you have?")
    selected = st.selectbox("Choose one", DISEASES, index=None, placeholder="Select a disease...")

    st.subheader("2) What symptoms are you experiencing?")
    txt = st.text_area(
        "Describe your symptoms (e.g., fatigue, brain fog, joint pain)",
        height=140
    )
    submitted = st.form_submit_button("💡 Get Remedy Recommendation")

# --- Only run the API request when the form is submitted ---
if submitted:
    if not selected:
        st.warning("⚠️ Please select a disease.")
    elif not txt.strip():
        st.warning("⚠️ Please describe your symptoms.")
    else:
        st.info("⏳ Generating your personalized remedy recommendation...")

        url = "https://remedyrecommenderimage-745821369635.europe-west1.run.app/recommend_remedies"

        params = {
            "disease": selected,
            "symptoms_text": txt
        }

        resp = requests.get(url, params=params, timeout=30)
        data = resp.json()
        recs = data.get("recommendations_list", [])

        if recs:
            st.success("✅ The recommended remedies are:")
            for r in recs:
                # Extract information from the text response
                parts = r.split("remedy for ")[1].split(" according to the ")
                symptom = parts[0].strip().capitalize()
                rest = parts[1]
                subreddit = rest.split("' subreddit is ")[0].replace("the '", "").replace("'", "").strip()
                remedy = rest.split("subreddit is ")[1].split(". It was")[0].strip()
                mentions = rest.split("mentioned ")[-1].split(" times")[0].strip()

                st.markdown(f"""
                <div style="
                    background-color: #f9f9f9;
                    border-left: 6px solid #4CAF50;
                    border-radius: 10px;
                    padding: 12px 16px;
                    margin-bottom: 10px;
                    box-shadow: 0px 2px 6px rgba(0,0,0,1);
                ">
                <h4 style="margin: 0; color: #2E7D32;">🧠 {symptom}</h4>
                <p style="margin: 4px 0;">
                    <b>Recommended Remedy:</b> {remedy}<br>
                    <b>Mentions:</b> {mentions} &nbsp;&nbsp; | &nbsp;&nbsp;
                    <b>Subreddit:</b> {subreddit}
                </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No remedy found in the response. Please check the API output format.")
