import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")

# Load data
df = pd.read_csv("cleaned_orders.csv", parse_dates=["Order Date"])
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)

# Sidebar filters
st.sidebar.title("Filters")
region = st.sidebar.multiselect("Select Region", options=df["Region"].unique(), default=df["Region"].unique())
category = st.sidebar.multiselect("Select Category", options=df["Category"].unique(), default=df["Category"].unique())

filtered_df = df[(df["Region"].isin(region)) & (df["Category"].isin(category))]

# ---- KPIs ----
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
return_rate = filtered_df["Returned"].mean() * 100

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"₹{total_sales:,.0f}")
col2.metric("📈 Total Profit", f"₹{total_profit:,.0f}")
col3.metric("🧾 Total Orders", f"{total_orders:,}")
col4.metric("🔁 Return Rate", f"{return_rate:.2f} %")

# Dashboard Title
st.title("🧮 Retail Data Dashboard")

# Row 1: Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")
monthly_sales = filtered_df.groupby('Month')['Sales'].sum().reset_index()
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', marker='o', ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Row 2: Sales by Region and Return Rate
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Sales by Region")
    region_sales = filtered_df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
    st.bar_chart(region_sales)

with col2:
    st.subheader("🔁 Return Rate by Region")
    return_rate = filtered_df.groupby('Region')['Returned'].mean()
    st.bar_chart(return_rate)

# Row 3: Top Products and Customers by Profit
col3, col4 = st.columns(2)

with col3:
    st.subheader("🏆 Top 5 Products by Profit")
    top_products = filtered_df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(5)
    st.bar_chart(top_products)

with col4:
    st.subheader("🏆 Top 5 Customers by Profit")
    top_customers = filtered_df.groupby('Customer Name')['Profit'].sum().sort_values(ascending=False).head(5)
    st.bar_chart(top_customers)

# Row 4: Most Returned Products
st.subheader("📦 Most Returned Products")
returned_products = filtered_df[filtered_df['Returned'] == 1]['Product Name'].value_counts().head(10)
st.bar_chart(returned_products)