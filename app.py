import streamlit as st
import pandas as pd

st.set_page_config(page_title="Delhivery Prototype", layout="centered")

st.title("🚚 Delhivery Route Optimization System")

menu = st.sidebar.radio("Navigation", ["Login", "Dashboard", "Route", "Traffic", "Status"])

if menu == "Login":
    st.subheader("Login")
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.button("Login")

elif menu == "Dashboard":
    st.subheader("Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Deliveries", "10")
    col2.metric("Delivered", "4")
    col3.metric("Pending", "6")
    st.button("Optimize Route")

elif menu == "Route":
    st.subheader("Optimized Route")
    st.error("Old Route: Warehouse → D → B → A → C")
    st.success("New Route: Warehouse → B → D → A → C")
    st.info("✔ Reduced distance and delivery time")

elif menu == "Traffic":
    st.subheader("Traffic Alert")
    st.warning("🚦 Heavy Traffic Detected")
    st.write("Route Updated Automatically")

elif menu == "Status":
    st.subheader("Delivery Status")
    df = pd.DataFrame({
        "Location": ["A","B","C","D"],
        "Status": ["Delivered","Delivered","Pending","Pending"]
    })
    st.table(df)
