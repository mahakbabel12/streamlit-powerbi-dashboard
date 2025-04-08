import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_custom_css

st.set_page_config(page_title="Smart Power BI Dashboard", layout="wide")
load_custom_css()

st.title("📊 Smart Power BI + Auto-Visualization Dashboard")
st.markdown("Upload your dataset and explore it instantly.")

uploaded_file = st.file_uploader("📂 Upload CSV or Excel File", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("✅ File uploaded successfully!")
        st.dataframe(df.head())

        st.subheader("📈 Auto Visualizations")

        num_cols = df.select_dtypes(include='number').columns
        cat_cols = df.select_dtypes(include='object').columns

        # 1️⃣ Correlation Heatmap
        if len(num_cols) >= 2:
            st.markdown("#### 🔥 Correlation Heatmap")
            fig, ax = plt.subplots()
            sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)

        # 2️⃣ Bar Chart for Top 5 by first numeric column
        if len(cat_cols) > 0 and len(num_cols) > 0:
            st.markdown(f"#### 📊 Top 5 `{cat_cols[0]}` by `{num_cols[0]}`")
            top5 = df.groupby(cat_cols[0])[num_cols[0]].sum().sort_values(ascending=False).head(5)
            st.bar_chart(top5)

        # 3️⃣ Pie Chart for first categorical column
        if len(cat_cols) > 0:
            st.markdown(f"#### 🧁 Category Breakdown: `{cat_cols[0]}`")
            fig2, ax2 = plt.subplots()
            df[cat_cols[0]].value_counts().plot.pie(autopct='%1.1f%%', ax=ax2)
            ax2.set_ylabel('')
            st.pyplot(fig2)

        # 4️⃣ Line Chart for Date column (auto-detected)
        lower_cols = df.columns.str.lower()
        if any('date' in col for col in lower_cols) and len(num_cols) > 0:
            date_col = [col for col in df.columns if 'date' in col.lower()][0]
            st.markdown(f"#### 📅 Time Series: `{date_col}` vs `{num_cols[0]}`")

            df[date_col] = pd.to_datetime(df[date_col], dayfirst=True, errors='coerce')
            ts_df = df.dropna(subset=[date_col])
            ts_df = ts_df.groupby(date_col)[num_cols[0]].sum().reset_index()

            st.line_chart(ts_df.set_index(date_col))

        # 5️⃣ Histograms for all numeric columns
        if len(num_cols) > 0:
            st.markdown("#### 📊 Histograms of Numeric Columns")
            for col in num_cols:
                st.markdown(f"**Histogram: `{col}`**")
                fig3, ax3 = plt.subplots()
                sns.histplot(df[col].dropna(), bins=20, kde=True, ax=ax3)
                st.pyplot(fig3)

    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.info("⬆️ Please upload a CSV or Excel file to begin.")
