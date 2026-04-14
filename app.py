import streamlit as st
import pandas as pd
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Delhivery Route Optimizer", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS FOR PREMIUM UI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Main Container */
    .main {
        background-color: #F8FAFC;
    }

    /* Modern Card UI */
    .stCard {
        background: white;
        padding: 24px;
        border-radius: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 20px;
    }

    /* Metrics Styling */
    .metric-box {
        text-align: center;
        padding: 15px;
        background: #FFFFFF;
        border-radius: 12px;
        border-left: 5px solid #2563EB;
    }

    /* Status Badges */
    .badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    .badge-delivered { background-color: #DCFCE7; color: #166534; }
    .badge-pending { background-color: #FEF9C3; color: #854D0E; }
    .badge-alert { background-color: #FEE2E2; color: #991B1B; }

    /* Custom Button */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background-color: #2563EB;
        color: white;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = 'Login'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def nav_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- SCREEN: LOGIN ---
if st.session_state.page == 'Login' and not st.session_state.logged_in:
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("https://upload.wikimedia.org/wikipedia/commons/a/ad/Delhivery_Logo_%282019%29.png", width=200)
        st.markdown("### Route Optimization System")
        with st.container():
            st.markdown('<div class="stCard">', unsafe_allow_html=True)
            username = st.text_input("Username", placeholder="admin@delhivery.com")
            password = st.text_input("Password", type="password")
            if st.button("Login"):
                st.session_state.logged_in = True
                nav_to('Dashboard')
            st.markdown('</div>', unsafe_allow_html=True)

# --- NAVIGATION BAR (Post-Login) ---
if st.session_state.logged_in:
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/a/ad/Delhivery_Logo_%282019%29.png", width=150)
        st.markdown("---")
        if st.button("📊 Dashboard"): nav_to('Dashboard')
        if st.button("🛣️ Optimize Route"): nav_to('Optimize')
        if st.button("⚠️ Traffic Alerts"): nav_to('Traffic')
        if st.button("📦 Delivery Status"): nav_to('Status')
        st.markdown("---")
        if st.button("Logout"):
            st.session_state.logged_in = False
            nav_to('Login')

    # --- SCREEN: DASHBOARD ---
    if st.session_state.page == 'Dashboard':
        st.title("Welcome back, Admin 👋")
        
        m1, m2, m3, m4 = st.columns(4)
        m1.markdown('<div class="metric-box"><h4>Total</h4><h2>1,284</h2></div>', unsafe_allow_html=True)
        m2.markdown('<div class="metric-box"><h4>Delivered</h4><h2 style="color:green">1,120</h2></div>', unsafe_allow_html=True)
        m3.markdown('<div class="metric-box"><h4>Pending</h4><h2 style="color:orange">154</h2></div>', unsafe_allow_html=True)
        m4.markdown('<div class="metric-box"><h4>Efficiency</h4><h2 style="color:#2563EB">+14%</h2></div>', unsafe_allow_html=True)

        st.markdown("### Active Fleet Map")
        st.map(pd.DataFrame({'lat': [28.61, 28.62, 28.63], 'lon': [77.20, 77.21, 77.22]}))

    # --- SCREEN: OPTIMIZATION ---
    elif st.session_state.page == 'Optimize':
        st.title("AI Route Optimization")
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown('<div class="stCard"><b>Legacy Route (Manual)</b><br>Total Distance: 42km<br>Est Time: 120 mins</div>', unsafe_allow_html=True)
            st.info("📍 Hub ➔ Sector 12 ➔ Okhla ➔ Rohini")
            
        with col_b:
            st.markdown('<div class="stCard"><b>Optimized Route (AI)</b><br>Total Distance: 34km<br>Est Time: 85 mins</div>', unsafe_allow_html=True)
            st.success("📍 Hub ➔ Okhla ➔ Sector 12 ➔ Rohini")

        if st.button("Apply Optimized Path"):
            with st.spinner("Calculating live traffic adjustments..."):
                time.sleep(1.5)
                st.balloons()
                st.success("Route pushed to driver apps successfully!")

    # --- SCREEN: TRAFFIC ---
    elif st.session_state.page == 'Traffic':
        st.title("Live Traffic Intelligence")
        st.markdown("""
            <div class="stCard" style="border-left: 8px solid #EF4444;">
                <h4 style="color:#991B1B;">⚠️ Major Congestion: NH-48</h4>
                <p>Accident reported near Cyber City. 25-minute delay expected for Fleet ID: <b>DEL-992</b>.</p>
            </div>
            <div class="stCard" style="border-left: 8px solid #F59E0B;">
                <h4 style="color:#854D0E;">🚧 Road Work: MG Road</h4>
                <p>Single lane traffic. Rerouting Fleet ID: <b>DEL-104</b> via alternate link road.</p>
            </div>
        """, unsafe_allow_html=True)

    # --- SCREEN: STATUS ---
    elif st.session_state.page == 'Status':
        st.title("Live Delivery Logs")
        data = {
            "Order ID": ["#DLV-1001", "#DLV-1002", "#DLV-1003", "#DLV-1004"],
            "Destination": ["South Ex, Delhi", "Indirapuram, GZB", "Dwarka Sec-10", "Noida Sec-62"],
            "Status": ["Delivered", "Pending", "Delivered", "Pending"]
        }
        df = pd.DataFrame(data)
        
        for index, row in df.iterrows():
            badge_class = "badge-delivered" if row["Status"] == "Delivered" else "badge-pending"
            st.markdown(f"""
                <div class="stCard">
                    <div style="display: flex; justify-content: space-between;">
                        <b>{row["Order ID"]}</b>
                        <span class="badge {badge_class}">{row["Status"]}</span>
                    </div>
                    <small>{row["Destination"]}</small>
                </div>
            """, unsafe_allow_html=True)
