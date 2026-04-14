import streamlit as st
import pandas as pd

st.set_page_config(page_title="Delhivery AI System", layout="wide")

# ---------- SESSION STATE ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "Login"

# ---------- STYLING ----------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.big-title {
    font-size:40px;
    font-weight:bold;
    color:#1E3A8A;
}
.card {
    padding:20px;
    border-radius:15px;
    background:white;
    box-shadow:0 4px 10px rgba(0,0,0,0.1);
    text-align:center;
}
.button {
    background-color:#2563EB;
    color:white;
    padding:10px;
    border-radius:10px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN PAGE ----------
if not st.session_state.logged_in:
    st.markdown('<p class="big-title">🚚 Delhivery Route Optimization</p>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            st.session_state.logged_in = True
            st.session_state.page = "Dashboard"
            st.success("Login Successful!")
        else:
            st.error("Enter valid credentials")

# ---------- MAIN APP ----------
if st.session_state.logged_in:

    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", ["Dashboard", "Route", "Traffic", "Status", "Logout"])

    # DASHBOARD
    if choice == "Dashboard":
        st.title("📊 Dashboard")

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Deliveries", "10")
        col2.metric("Delivered", "4")
        col3.metric("Pending", "6")

        if st.button("Optimize Route"):
            st.session_state.page = "Route"

    # ROUTE
    elif choice == "Route":
        st.title("🗺️ Optimized Route")

        st.error("Old Route: Warehouse → D → B → A → C")
        st.success("Optimized Route: Warehouse → B → D → A → C")

        st.info("✔ Reduced distance by 25%")

    # TRAFFIC
    elif choice == "Traffic":
        st.title("🚦 Traffic Alert")

        st.warning("Heavy Traffic Detected!")
        st.success("Route Updated Automatically")

    # STATUS
    elif choice == "Status":
        st.title("📦 Delivery Status")

        df = pd.DataFrame({
            "Location": ["A", "B", "C", "D"],
            "Status": ["Delivered", "Delivered", "Pending", "Pending"]
        })

        st.dataframe(df, use_container_width=True)

    # LOGOUT
    elif choice == "Logout":
        st.session_state.logged_in = False
        st.experimental_rerun()
