import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import json
from streamlit_lottie import st_lottie

# ---- SAFE CV2 IMPORT ----
try:
    import cv2
    camera_available = True
except:
    camera_available = False

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# Fixed credentials
USERNAME = "optimizers"
PASSWORD = "homi@2004"

# Session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# ---- LOGIN ----
def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["logged_in"] = True
            st.rerun()  # 🔥 instantly go to home page
        else:
            st.error("Invalid username or password")

# ---- MAIN ----
if not st.session_state["logged_in"]:
    login()
else:
    st.sidebar.title("🤖 Automorphic")
    page = st.sidebar.selectbox("Navigation", ["Home","Live Sensor Data","Springback Detection","Analytics Dashboard","Simulation Mode","Documentation","About","Help / Support"])

    if page == "Home":
        st.title("🚀 Automorphic")

        # ---- HERO SECTION ----
        st.markdown("""
        <h3 style='text-align: center;'>
        Redefining Precision in Automobile Manufacturing
        </h3>
        <p style='text-align: center; font-size:18px;'>
        AI + IoT powered intelligence for next-generation metal forming
        </p>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # ---- PROBLEM + SOLUTION ----
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("⚠️ The Problem")
            st.write("""
            In traditional automobile manufacturing, achieving precise metal curvature 
            is difficult due to the **springback effect**, where metal returns toward 
            its original shape after deformation.
            """)

        with col2:
            st.subheader("✅ Our Solution")
            st.write("""
            Automorphic uses **IoT sensors + Machine Learning** to predict the exact 
            conditions required for metal shaping — minimizing error and maximizing precision.
            """)

        st.markdown("---")

        # ---- FEATURES ----
        st.subheader("⚙️ Core Capabilities")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### 📡 Smart Sensing")
            st.write("""
            - Temperature monitoring  
            - Metal thickness detection  
            - IR-based presence sensing  
            - Material properties (Young’s Modulus)
            """)

        with col2:
            st.markdown("### 🧠 ML Prediction")
            st.write("""
            - Predict optimal **force & temperature**  
            - Adaptive learning from data  
            - Real-time decision making  
            """)

        with col3:
            st.markdown("### 🎥 Vision Validation")
            st.write("""
            - Camera-based inspection  
            - Detect springback effect  
            - Ensure curvature accuracy  
            """)

        st.markdown("---")

        # ---- WORKFLOW ----
        st.subheader("🔄 How It Works")

        st.write("""
        1. 📡 IoT sensors collect real-time data (temperature, thickness, presence)  
        2. 🧠 ML model predicts required force & optimal conditions  
        3. ⚙️ Metal shaping process is executed  
        4. 🎥 Camera validates curvature and detects springback  
        5. 🔁 System improves continuously using feedback  
        """)

        st.markdown("---")

        # ---- IMPACT ----
        st.subheader("🌍 Impact")

        st.success("""
        🚗 Higher precision in automobile manufacturing  
        💰 Reduced material wastage  
        ⚡ Faster and smarter production  
        🔬 Data-driven industrial automation  
        """)

        st.markdown("---")

        # ---- TAGLINE ----
        st.markdown("""
        <h4 style='text-align: center; color: grey;'>
        Automorphic isn’t just automation — it’s intelligent transformation.
        </h4>
        """, unsafe_allow_html=True)

    elif page == "Live Sensor Data":
        # st.title("📡 Live Sensor Dashboard")

        # st.markdown("### Real-Time IoT Sensor Monitoring")

        # # ---- AUTO REFRESH ----
        # refresh = st.button("🔄 Refresh Data")

        # # Dummy sensor values (simulate real-time variation)
        # temperature = round(random.uniform(25, 80), 2)
        # thickness = round(random.uniform(1.0, 5.0), 2)
        # metal_present = random.choice(["Yes", "No"])
        # young_modulus = round(random.uniform(150, 220), 2)  # GPa

        # st.markdown("---")

        # # ---- METRICS ----
        # col1, col2, col3, col4 = st.columns(4)

        # with col1:
        #     st.metric("🌡 Temperature (°C)", temperature)

        # with col2:
        #     st.metric("📏 Thickness (mm)", thickness)

        # with col3:
        #     st.metric("🔴 Metal Presence", metal_present)

        # with col4:
        #     st.metric("⚙️ Young’s Modulus (GPa)", young_modulus)

        # st.markdown("---")

        # # ---- STATUS INDICATOR ----
        # st.subheader("🟢 System Status")

        # if metal_present == "Yes":
        #     st.success("Metal Sheet Detected - System Ready")
        # else:
        #     st.error("No Metal Detected - Waiting for Input")

        # # ---- SENSOR DETAILS ----
        # st.subheader("📊 Sensor Insights")

        # st.write(f"""
        # - Current temperature is **{temperature}°C**, affecting material flexibility  
        # - Sheet thickness detected: **{thickness} mm**  
        # - Young’s Modulus indicates material stiffness: **{young_modulus} GPa**  
        # """)

        # st.markdown("---")

        # st.info("📡 Data is currently simulated. In production, values will be fetched from IoT cloud.")
        # ---- SESSION STATE INIT ----
        st.title("📡 Live Sensor Dashboard")

        # ---- SESSION STATE INIT ----
        if "sensor_data" not in st.session_state:
            st.session_state.sensor_data = {
                "temperature": 30,
                "thickness": 2.0,
                "metal_present": "Yes",
                "young_modulus": 180
            }

        # ---- REFRESH BUTTON ----
        if st.button("🔄 Refresh Data"):
            st.session_state.sensor_data = {
                "temperature": round(random.uniform(25, 80), 2),
                "thickness": round(random.uniform(1.0, 5.0), 2),
                "metal_present": random.choice(["Yes", "No"]),
                "young_modulus": round(random.uniform(150, 220), 2)
            }

        data = st.session_state.sensor_data

        st.markdown("---")

        # ---- METRICS ----
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("🌡 Temperature (°C)", data["temperature"])
        col2.metric("📏 Thickness (mm)", data["thickness"])
        col3.metric("🔴 Metal Presence", data["metal_present"])
        col4.metric("⚙️ Young’s Modulus (GPa)", data["young_modulus"])

        st.markdown("---")

        # ---- STATUS ----
        if data["metal_present"] == "Yes":
            st.success("Metal Sheet Detected - System Ready")
        else:
            st.error("No Metal Detected")

        st.markdown("---")

        # ---- ML INSIGHTS ----
        show_ml = st.toggle("🧠 Show ML Insights")

        if show_ml:
            st.subheader("🧠 ML Prediction Insights")

            angle = st.slider("🎯 Target Curvature Angle (degrees)", 0, 180, 90)

            # ---- ML LOGIC ----
            base_force = data["thickness"] * data["young_modulus"] * angle * 0.5
            temp_factor = max(0.5, 1 - (data["temperature"] / 200))
            predicted_force = round(base_force * temp_factor, 2)

            optimal_temp = round(
                data["temperature"] + (angle / 10) + (data["thickness"] * 2), 2
            )

            # ---- OUTPUT ----
            c1, c2 = st.columns(2)

            c1.success(f"💪 Required Force: {predicted_force} N")
            c2.success(f"🔥 Optimal Temperature: {optimal_temp} °C")

            st.info(f"""
            Based on current sensor readings:
            - Temperature: {data["temperature"]}°C  
            - Thickness: {data["thickness"]} mm  
            - Young’s Modulus: {data["young_modulus"]} GPa  

            The system predicts optimal forming conditions to minimize springback.
            """)
    
    elif page == "Springback Detection":
        st.title("🎥 Live Springback Detection")

        st.markdown("### Recording live metal deformation (40 seconds)")

        # ---- CHECK CAMERA AVAILABILITY ----
        if not camera_available:
            st.warning("📷 Live camera is not supported in cloud deployment.")
            st.info("👉 Please run this app locally to use the camera feature.")
    
        else:
            start = st.button("▶️ Start Recording")
    
            if start:
                cap = cv2.VideoCapture(0)
    
                stframe = st.empty()
    
                start_time = time.time()
                duration = 40  # seconds
    
                while True:
                    ret, frame = cap.read()
    
                    if not ret:
                        st.error("Camera not working")
                        break
    
                    # Convert BGR to RGB
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
                    # Display frame
                    stframe.image(frame, channels="RGB")
    
                    # Stop after duration
                    if time.time() - start_time > duration:
                        break
    
                cap.release()
    
                st.success("✅ Recording Complete")
    
                # ---- SIMULATED SPRINGBACK RESULT ----
                springback = round(random.uniform(2, 10), 2)
    
                st.markdown("## 📊 Springback Analysis")
    
                st.metric("📉 Springback Effect", f"{springback}°")
    
                if springback < 3:
                    st.success("Springback within limits")
                elif springback < 7:
                    st.warning("Moderate springback detected")
                else:
                    st.error("High springback - correction needed")
    
    elif page == "Analytics Dashboard":
        with col2:
            st_lottie(lottie_analysis, height=550)

        # ---- LOAD LOTTIE ----
        lottie_analysis = load_lottiefile("analysis.json")

        # ---- CENTERED ANIMATION ----
        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            st_lottie(lottie_analysis, height=550)

        st.markdown("### Live Industrial Data Insights")

        # ---- SESSION STATE ----
        if "history" not in st.session_state:
            st.session_state.history = {
                "temperature": [],
                "force": [],
                "thickness": []
            }

        # ---- REFRESH BUTTON ----
        if st.button("🔄 Generate Data"):
            for _ in range(10):
                temp = random.uniform(25, 80)
                thickness = random.uniform(1, 5)

                # Fake force relation
                force = temp * thickness * random.uniform(5, 10)

                st.session_state.history["temperature"].append(temp)
                st.session_state.history["force"].append(force)
                st.session_state.history["thickness"].append(thickness)

        data = st.session_state.history

        # ---- TEMPERATURE GRAPH ----
        if data["temperature"]:
            st.subheader("🌡 Temperature Trend")

            fig1, ax1 = plt.subplots()
            ax1.plot(data["temperature"])
            ax1.set_xlabel("Time")
            ax1.set_ylabel("Temperature (°C)")
            st.pyplot(fig1)

        # ---- FORCE VS TEMPERATURE ----
        if data["force"]:
            st.subheader("💪 Force vs Temperature")

            fig2, ax2 = plt.subplots()
            ax2.scatter(data["temperature"], data["force"])
            ax2.set_xlabel("Temperature (°C)")
            ax2.set_ylabel("Force (N)")
            st.pyplot(fig2)

        # ---- THICKNESS GRAPH ----
        if data["thickness"]:
            st.subheader("📏 Thickness Variation")

            fig3, ax3 = plt.subplots()
            ax3.plot(data["thickness"])
            ax3.set_xlabel("Time")
            ax3.set_ylabel("Thickness (mm)")
            st.pyplot(fig3)

        st.markdown("---")

        st.info("📊 Data is simulated for demonstration purposes.")                
    
    elif page == "Simulation Mode":
        st.title("⚙️ Simulation Mode")

        st.markdown("### Test Different Conditions & Analyze Results")

        st.markdown("---")

        # ---- INPUTS ----
        col1, col2 = st.columns(2)

        with col1:
            temperature = st.slider("🌡 Temperature (°C)", 20, 100, 40)
            thickness = st.slider("📏 Thickness (mm)", 1.0, 5.0, 2.5)

        with col2:
            young_modulus = st.slider("⚙️ Young’s Modulus (GPa)", 150, 220, 180)
            angle = st.slider("🎯 Target Curvature Angle (degrees)", 0, 180, 90)

        st.markdown("---")

        # ---- RUN SIMULATION ----
        if st.button("🚀 Run Simulation"):

            # ---- ML LOGIC ----
            base_force = thickness * young_modulus * angle * 0.5
            temp_factor = max(0.5, 1 - (temperature / 200))

            predicted_force = round(base_force * temp_factor, 2)
            optimal_temp = round(temperature + (angle / 10) + (thickness * 2), 2)

            # Simulated springback
            springback = round((angle * 0.05) + (thickness * 0.5) - (temperature * 0.02), 2)

            st.markdown("## 📊 Simulation Results")

            col1, col2, col3 = st.columns(3)

            col1.metric("💪 Force Required", f"{predicted_force} N")
            col2.metric("🔥 Optimal Temp", f"{optimal_temp} °C")
            col3.metric("📉 Springback", f"{springback}°")

            st.markdown("---")

            # ---- INTERPRETATION ----
            st.subheader("🧠 Insights")

            st.write(f"""
            - Increasing **temperature ({temperature}°C)** reduces required force  
            - Higher **thickness ({thickness} mm)** increases resistance  
            - **Young’s Modulus ({young_modulus} GPa)** affects stiffness  
            - Predicted springback: **{springback}°**

            ✅ Adjust temperature and force to minimize springback.
            """)

            st.markdown("---")

            # ---- SIMPLE GRAPH ----
            import matplotlib.pyplot as plt

            temps = list(range(20, 100, 5))
            forces = [
                (thickness * young_modulus * angle * 0.5) * max(0.5, 1 - (t / 200))
                for t in temps
            ]

            fig, ax = plt.subplots()
            ax.plot(temps, forces)
            ax.set_xlabel("Temperature (°C)")
            ax.set_ylabel("Force (N)")
            ax.set_title("Force vs Temperature")

            st.pyplot(fig)
    
    elif page == "Documentation":
        
        # ---- LOAD LOTTIE ----
        lottie_analysis = load_lottiefile("Documentation.json")

        # ---- CENTERED ANIMATION ----
        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            st_lottie(lottie_analysis, height=550)

        st.markdown("### Automorphic: Smart IoT-Based Metal Forming System")

        st.markdown("---")

        # ---- OVERVIEW ----
        st.header("🔍 Overview")

        st.write("""
        Automorphic is an intelligent IoT-based system designed to optimize 
        metal sheet deformation in automobile manufacturing. It integrates 
        real-time sensor data, machine learning prediction, and computer vision 
        to minimize the springback effect and improve production accuracy.
        """)

        st.markdown("---")

        # ---- SYSTEM ARCHITECTURE ----
        st.header("🏗 System Architecture")

        st.write("""
        The system follows a multi-stage pipeline:

        1. 📡 **IoT Sensors Layer**  
        - Temperature Sensor  
        - Thickness Measurement  
        - IR Sensor (Metal Detection)  
        - Material Properties (Young’s Modulus)

        2. 🧠 **ML Prediction Layer**  
        - Predicts optimal force and temperature  
        - Uses input parameters to minimize deformation error  

        3. 🎥 **Vision Layer**  
        - Captures metal sheet after deformation  
        - Detects final curvature  
        - Calculates springback effect  

        4. 📊 **Analytics Layer**  
        - Visualizes trends and relationships  
        - Helps in decision-making  

        5. ⚙️ **Simulation Layer**  
        - Allows testing under different conditions  
        - Acts as a virtual environment for experimentation  
        """)

        st.markdown("---")

        # ---- WORKFLOW ----
        st.header("🔄 Workflow")

        st.write("""
        1. Sensors collect real-time industrial data  
        2. Data is sent to cloud/server  
        3. ML model predicts required force and temperature  
        4. Metal forming process is executed  
        5. Camera captures final output  
        6. Springback effect is analyzed  
        7. Feedback improves future predictions  
        """)

        st.markdown("---")

        # ---- TECHNOLOGIES ----
        st.header("🛠 Technologies Used")

        st.write("""
        - **Frontend:** Streamlit  
        - **Backend:** Python  
        - **Machine Learning:** Custom predictive logic  
        - **Computer Vision:** OpenCV  
        - **IoT Integration:** Sensor-based data acquisition  
        - **Visualization:** Matplotlib  
        """)

        st.markdown("---")

        # ---- FEATURES ----
        st.header("✨ Key Features")

        st.write("""
        - Real-time sensor monitoring  
        - ML-based prediction engine  
        - Springback detection using vision  
        - Interactive analytics dashboard  
        - Simulation mode for testing  
        """)

        st.markdown("---")

        # ---- FUTURE SCOPE ----
        st.header("🚀 Future Scope")

        st.write("""
        - Integration with real industrial IoT hardware  
        - Deployment on cloud platforms  
        - Advanced ML models (Neural Networks)  
        - Real-time video processing for accurate angle detection  
        - Integration with manufacturing control systems  
        """)

        st.markdown("---")

        # ---- CONCLUSION ----
        st.header("✅ Conclusion")

        st.write("""
        Automorphic provides a smart and scalable solution for improving 
        metal forming processes in the automobile industry. By combining IoT, 
        ML, and computer vision, it reduces errors, minimizes waste, and enhances 
        production efficiency.
        """)
        
    elif page == "About":
        # ---- LOAD LOTTIE ----
        lottie_analysis = load_lottiefile("about.json")

        # ---- CENTERED ANIMATION ----
        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            st_lottie(lottie_analysis, height=550)

        st.markdown("### Smart IoT-Based Metal Forming System")

        st.markdown("---")

        # ---- PRODUCT OVERVIEW ----
        st.header("📌 About the Product")

        st.write("""
        **Automorphic** is an intelligent IoT-based system designed to enhance 
        precision in automobile manufacturing, specifically in metal sheet deformation.

        The system integrates **IoT sensors, Machine Learning, and Computer Vision**
        to predict and control the bending process of metal sheets. By analyzing 
        parameters such as temperature, thickness, and material properties 
        (Young’s Modulus), Automorphic determines the optimal force and conditions 
        required for accurate shaping.

        A key challenge in metal forming is the **springback effect**, where the metal 
        tends to revert toward its original shape after deformation. Automorphic 
        addresses this by combining predictive modeling with real-time validation 
        using camera-based analysis.

        This results in:
        - Higher precision in curvature  
        - Reduced material wastage  
        - Improved manufacturing efficiency  
        - Data-driven industrial decision-making  
        """)

        st.markdown("---")

        # ---- TEAM SECTION ----
        st.header("👥 Team")

        st.subheader("🔹 Core Roles")

        st.write("""
        **Aditya Sarkar**  
        *Team SPOC*  

        **Toshikka G**  
        *Team Reviewer*  
        """)

        st.markdown("---")

        st.subheader("🔹 Team Members")

        st.write("""
        - Atul Atul  
        - Anagha Giri  
        - V Nisha
        - Sanjay Gadde  
        """)

        st.markdown("---")

        # ---- PROJECT NOTE ----
        st.success("🚀 Developed under the TCS ILP initiative, focusing on AI, IoT, and Smart Manufacturing solutions")

    elif page == "Help / Support":
        
         # ---- LOAD LOTTIE ----
        lottie_analysis = load_lottiefile("call-center.json")

        # ---- CENTERED ANIMATION ----
        col1, col2, col3 = st.columns([1, 3, 1])

        with col2:
            st_lottie(lottie_analysis, height=550)

        st.markdown("### How to Use Automorphic")

        st.markdown("---")

        # ---- OVERVIEW ----
        st.header("📌 Overview")

        st.write("""
        Automorphic is a smart IoT-based platform designed to assist in metal sheet 
        deformation and springback analysis. This guide will help you navigate and 
        use different features of the system effectively.
        """)

        st.markdown("---")

        # ---- SENSOR DASHBOARD ----
        st.header("📡 Sensor Dashboard")

        st.write("""
        - Click **'Refresh Data'** to generate simulated real-time sensor values  
        - View parameters like temperature, thickness, metal presence, and material properties  
        - Toggle **'Show ML Insights'** to view predictions based on current data  
        """)

        st.markdown("---")

        # ---- ML INSIGHTS ----
        st.header("🧠 ML Insights")

        st.write("""
        - Adjust the **target angle** to simulate different bending requirements  
        - The system predicts:
            - Required force  
            - Optimal temperature  
        - Results are based on real-time sensor values  
        """)

        st.markdown("---")

        # ---- SPRINGBACK DETECTION ----
        st.header("🎥 Springback Detection")

        st.write("""
        - Click **'Start Recording'** to begin live video capture  
        - The system records for a few seconds  
        - After recording, it estimates the **springback effect**  
        """)

        st.markdown("---")

        # ---- ANALYTICS ----
        st.header("📊 Analytics Dashboard")

        st.write("""
        - Click **'Generate Data'** to create sample datasets  
        - View graphs such as:
            - Temperature trends  
            - Force vs Temperature  
            - Thickness variation  
        """)

        st.markdown("---")

        # ---- SIMULATION ----
        st.header("⚙️ Simulation Mode")

        st.write("""
        - Manually adjust parameters like temperature, thickness, and angle  
        - Click **'Run Simulation'** to analyze results  
        - Useful for testing different industrial scenarios  
        """)

        st.markdown("---")

        # ---- TROUBLESHOOTING ----
        st.header("🛠 Troubleshooting")

        st.write("""
        - If camera does not open, ensure webcam permissions are enabled  
        - If graphs do not appear, click the generate button again  
        - Refresh the page if any module stops responding  
        """)

        st.markdown("---")

        # ---- CONTACT ----
        st.header("📞 Support")

        st.write("""
        For any issues or queries, please contact the development team:
        """)

        st.markdown("""
        📧 **Email:** adi.sarkar2004@gmail.com  
        📱 **Phone:** +91 8989028700  
        """)

        st.success("✅ You're ready to explore Automorphic!")

    # Logout
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()
