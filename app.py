import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import requests
from streamlit_lottie import st_lottie

# ---------- CONFIG ----------
st.set_page_config(page_title="Delhivery AI System", layout="wide")

# ---------- LOTTIE ----------
def load_lottie(url):
    return requests.get(url).json()

truck_anim = load_lottie("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")

# ---------- STYLING ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
}
.card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-6px) scale(1.02);
}
.big-title {
    font-size: 40px;
    font-weight: bold;
    color: #1E3A8A;
}
.stButton>button {
    border-radius: 10px;
    height: 45px;
    background: linear-gradient(90deg, #2563EB, #4F46E5);
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION ----------
if "login" not in st.session_state:
    st.session_state.login = False

# ---------- LOGIN ----------
if not st.session_state.login:
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st_lottie(truck_anim, height=200)
        st.markdown('<p class="big-title">Delhivery AI System</p>', unsafe_allow_html=True)

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username and password:
                st.session_state.login = True
                st.rerun()
            else:
                st.error("Enter credentials")

# ---------- MAIN APP ----------
if st.session_state.login:

    st.sidebar.title("🚚 Navigation")
    page = st.sidebar.radio("Go to", ["Dashboard", "Route AI", "Traffic", "Analytics", "Logout"])

    # ---------- DASHBOARD ----------
    if page == "Dashboard":
        st.title("📊 Smart Dashboard")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Total", "1,284")
        c2.metric("Delivered", "1,120")
        c3.metric("Pending", "154")
        c4.metric("Efficiency", "+14%")

        st_lottie(truck_anim, height=150)

        # PIE CHART
        data = pd.DataFrame({
            "Status": ["Delivered", "Pending"],
            "Count": [1120, 154]
        })

        fig = px.pie(data, names="Status", values="Count", hole=0.5,
                     color_discrete_sequence=["#22c55e", "#f59e0b"])
        st.plotly_chart(fig, use_container_width=True)

    # ---------- ROUTE ----------
    elif page == "Route AI":
        st.title("🧠 AI Route Optimization")

        col1, col2 = st.columns(2)

        with col1:
            st.error("Old Route")
            st.write("Warehouse → D → B → A → C")
            st.write("Distance: 42km | Time: 120 min")

        with col2:
            st.success("Optimized Route")
            st.write("Warehouse → B → D → A → C")
            st.write("Distance: 34km | Time: 85 min")

        if st.button("Optimize with AI"):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i+1)

            st.success("🚀 Route Optimized Successfully!")
            st.balloons()

        # MAP
        map_data = pd.DataFrame({
            "lat": [28.61, 28.62, 28.63, 28.65],
            "lon": [77.20, 77.21, 77.22, 77.25]
        })

        st.map(map_data)

    # ---------- TRAFFIC ----------
    elif page == "Traffic":
        st.title("🚦 Traffic Intelligence")

        st.error("⚠️ Heavy Traffic on NH-48")
        st.warning("🚧 Roadblock near MG Road")

        # BAR CHART
        traffic_data = pd.DataFrame({
            "Area": ["NH-48", "MG Road", "Noida", "Dwarka"],
            "Delay": [25, 15, 10, 5]
        })

        fig = px.bar(traffic_data, x="Area", y="Delay",
                     color="Delay", color_continuous_scale="reds")
        st.plotly_chart(fig, use_container_width=True)

    # ---------- ANALYTICS ----------
    elif page == "Analytics":
        st.title("📈 Advanced Analytics")

        df = pd.DataFrame({
            "Days": ["Mon","Tue","Wed","Thu","Fri"],
            "Deliveries": [200, 240, 300, 280, 350]
        })

        fig = px.line(df, x="Days", y="Deliveries", markers=True)
        st.plotly_chart(fig, use_container_width=True)

    # ---------- LOGOUT ----------
    elif page == "Logout":
        st.session_state.login = False
        st.rerun()
