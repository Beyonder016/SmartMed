import streamlit as st
import pandas as pd
import os
import sys
from datetime import datetime, timedelta
import plotly.express as px
import time
import base64

# Set Streamlit page config first
st.set_page_config(page_title="SmartMed Dashboard", page_icon="💊", layout="wide")

# Extend path to utils directory
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
from data_cleaning import clean_sales_data

# Inject custom CSS
def inject_custom_css():
    with open("styles/custom.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

inject_custom_css()

# Load and encode the GIF logo
@st.cache_data(show_spinner=False)
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_data = get_base64_image("assets/logo.gif")

# Sidebar branding with embedded base64 gif
with st.sidebar:
    st.markdown(
        f"""
        <div style='text-align:center; padding: 0.5rem 0;'>
            <img src='data:image/gif;base64,{logo_data}' width='80'/>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("### 🧠 SmartMed Analytics")
    st.markdown("Built for pharmacy distributors to unlock deep insights from Excel sales data.")

st.title("💊 SmartMed Sales Analytics Dashboard")
st.markdown("Upload your sales report (.xlsx or .csv) and let's crunch some pharmacy numbers like legends.")

uploaded_file = st.file_uploader("📤 Upload Sales Report", type=["xlsx", "csv"])

if uploaded_file:
    try:
        with st.spinner("Crunching numbers like a pharmacist on Red Bull..."):
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file, skiprows=6)

            df = clean_sales_data(df)

        st.write("🌸 Cleaned Columns:", df.columns.tolist())
        st.success("✅ File loaded and cleaned. Here's a preview:")
        st.dataframe(df.head(20), use_container_width=True)

        # Filters
        st.markdown("---")
        st.subheader("🎛️ Filter Options")

        min_date = df["Vch_date"].min()
        max_date = df["Vch_date"].max()

        with st.expander("🔎 Filters"):
            selected_date = st.date_input("Select Date Range", [min_date, max_date])
            selected_customer = st.selectbox("Select Customer", options=['All'] + sorted(df['Particulars'].dropna().unique().tolist()))
            selected_product = st.selectbox("Select Product", options=['All'] + sorted(df['Unnamed_1'].dropna().unique().tolist()))

        filtered_df = df.copy()
        if len(selected_date) == 2:
            start_date, end_date = pd.to_datetime(selected_date)
            filtered_df = filtered_df[(filtered_df["Vch_date"] >= start_date) & (filtered_df["Vch_date"] <= end_date)]

        if selected_customer != "All":
            filtered_df = filtered_df[filtered_df["Particulars"] == selected_customer]

        if selected_product != "All":
            filtered_df = filtered_df[filtered_df["Unnamed_1"] == selected_product]

        st.success(f"✅ Showing {len(filtered_df)} records after applying filters.")
        st.dataframe(filtered_df.head(20), use_container_width=True)

        # Export
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=filtered_df.to_csv(index=False).encode("utf-8"),
            file_name="filtered_sales_data.csv",
            mime="text/csv"
        )

        # KPI Metrics
        st.markdown("---")
        st.subheader("📊 Sales Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("💰 Total Sales", f"₹ {filtered_df['Amount'].sum():,.2f}")
        with col2:
            st.metric("📦 Quantity Sold", int(filtered_df['Qty'].sum()))
        with col3:
            st.metric("🎯 Avg Discount", f"₹ {filtered_df['Scm_disc'].mean():.2f}")
        with col4:
            exp_limit = datetime.now() + timedelta(days=90)
            if "Exp_date" in filtered_df.columns:
                upcoming_exp = filtered_df[filtered_df["Exp_date"] < exp_limit]
                st.metric("⏰ Expiring Batches", len(upcoming_exp))

        # Monthly Sales Trend
        with st.expander("📅 Monthly Sales Trend"):
            filtered_df["Month"] = filtered_df["Vch_date"].dt.to_period("M").astype(str)
            trend_df = filtered_df.groupby("Month", as_index=False)["Amount"].sum()
            trend_df["Month"] = pd.to_datetime(trend_df["Month"])
            trend_df = trend_df.sort_values("Month")
            trend_df["Month"] = trend_df["Month"].dt.strftime('%b %Y')

            fig = px.bar(trend_df, x="Month", y="Amount", text_auto=".2s",
                         title="📈 Monthly Sales (₹)", labels={"Amount": "₹ Sales"})
            fig.update_layout(xaxis_title="Month", yaxis_title="₹ Sales", xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)

        # Customer & Product Insights
        with st.expander("🧍‍♂️ Customer & Product Insights"):
            cust_df = filtered_df.groupby("Particulars")["Amount"].sum().nlargest(5).reset_index()
            fig1 = px.bar(cust_df, x="Amount", y="Particulars", orientation="h", title="Top 5 Customers by Revenue")
            st.plotly_chart(fig1, use_container_width=True)

            prod_df = filtered_df.groupby("Unnamed_1")["Qty"].sum().nlargest(5).reset_index()
            fig2 = px.bar(prod_df, x="Qty", y="Unnamed_1", orientation="h", title="Top 5 Products by Quantity Sold")
            st.plotly_chart(fig2, use_container_width=True)

        # Discount Effectiveness
        with st.expander("🎯 Discount Effectiveness"):
            df_clean = filtered_df[['Scm_disc', 'Amount']].dropna()

            def bucket_discount(disc):
                if disc <= 10:
                    return "Low (₹0-10)"
                elif disc <= 50:
                    return "Medium (₹10-50)"
                return "High (₹50+)"

            df_clean["Discount_Level"] = df_clean["Scm_disc"].apply(bucket_discount)

            fig_disc = px.scatter(df_clean, x="Scm_disc", y="Amount", color="Discount_Level",
                                  title="Discount vs Sales – Color by Discount Level")
            fig_disc.update_layout(xaxis_title="₹ Discount", yaxis_title="₹ Sales")
            st.plotly_chart(fig_disc, use_container_width=True)

        # Expiry
        with st.expander("⏳ Expiring Inventory"):
            exp_soon = filtered_df[filtered_df["Exp_date"] < datetime.now() + timedelta(days=90)]
            if not exp_soon.empty:
                exp_soon["Exp_date"] = pd.to_datetime(exp_soon["Exp_date"]).dt.date
                exp_df = exp_soon.groupby(["Exp_date", "Unnamed_1"])["Amount"].sum().reset_index()
                fig_exp = px.bar(exp_df, x="Exp_date", y="Amount", color="Unnamed_1",
                                 title="💀 Products Nearing Expiry (Next 90 Days)",
                                 labels={"Amount": "₹ Value", "Unnamed_1": "Product"})
                fig_exp.update_layout(barmode="group")
                st.plotly_chart(fig_exp, use_container_width=True)
            else:
                st.info("No stock expiring in the next 90 days.")

        # Footer
        st.markdown("""
        ---
        <p style='text-align:center; font-size:0.9rem;'>
        Built with ❤️ using Streamlit | © 2025 SmartMed Solutions
        </p>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"💥 Uh-oh! Something exploded. Error: {e}")
else:
    st.info("👈 Upload a file to get the magic started.")
