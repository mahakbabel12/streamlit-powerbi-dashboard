import streamlit as st

st.sidebar.markdown("## 🔧 Filters")
region = st.sidebar.selectbox("Select Region", ["All", "North", "South", "East", "West"])
category = st.sidebar.selectbox("Select Category", ["All", "Beverages", "Food", "Accessories"])

st.markdown("## 📌 Key Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Sales", value="$126K", delta="+12%")
with col2:
    st.metric(label="Units Sold", value="18.2K", delta="+7.5%")
with col3:
    st.metric(label="Returning Customers", value="4.3K", delta="-1.3%")
