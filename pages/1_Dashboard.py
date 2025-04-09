import streamlit as st
from streamlit.components.v1 import html

st.markdown("### 🔍 Live Power BI Dashboard")

# Replace this with your actual Power BI embed URL
powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=0ca9fbde-75d5-4528-b332-0568ad5e2d15&autoAuth=true&ctid=f8fdcadc-a212-41dd-b543-c6e2f23d970c"

html(
    f"""
    <iframe 
        title="Power BI Report"
        width="100%" 
        height="800" 
        src="{powerbi_url}" 
        frameborder="0" 
        allowFullScreen="true">
    </iframe>
    """,
    height=820,
)
