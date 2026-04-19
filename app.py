import streamlit as st

# Page config
st.set_page_config(
    page_title="Automorphic",
    page_icon="🤖",
    layout="wide"
)

# ---- SIDEBAR ----
st.sidebar.title("Automorphic")
st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home", "About", "Help"]
)

# ---- HOME PAGE ----
if page == "Home":
    st.title("🤖 Automorphic")
    st.subheader("Transforming Intelligence into Action")

    st.write(
        "Welcome to Automorphic – an AI-powered platform that adapts and evolves."
    )

    st.markdown("---")

    st.header("🚀 Features")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("🤖 Smart AI")

    with col2:
        st.write("⚡ Fast Processing")

    with col3:
        st.write("🔒 Secure")

# ---- ABOUT PAGE ----
elif page == "About":
    st.title("📖 About Automorphic")

    st.write(
        """
        Automorphic is a next-gen AI system designed to automate tasks,
        analyze data, and improve decision-making using machine learning.
        """
    )

# ---- HELP PAGE ----
elif page == "Help":
    st.title("❓ Help & Support")

    st.write("If you face any issues, contact support.")

    st.info("Email: support@automorphic.ai")