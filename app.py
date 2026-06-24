import streamlit as st
import re

st.set_page_config(
    page_title="Noise Pollution Study-Zone Finder",
    page_icon="🔊",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Prompt Engineering AI Analyzer",
        "Study-Zone Finder",
        "About Project"
    ]
)

if page == "Home":
    st.title("🔊 Noise Pollution Reporting and Study-Zone Finder")

    st.write("""
    This website helps students identify whether a location is suitable for studying.
    It uses Prompt Engineering to analyze noise pollution complaints.
    """)

    st.subheader("Project Features")
    st.write("""
    - Analyze noise pollution complaints using Prompt Engineering
    - Detect noise source and noise level
    - Classify study-zone suitability
    - Provide recommendations for students
    """)

elif page == "Prompt Engineering AI Analyzer":
    st.title("🤖 Prompt Engineering Noise Analyzer")

    st.write("""
    Enter a noise complaint. The system creates a structured prompt and analyzes
    the complaint using noise-level rules.
    """)

    complaint = st.text_area(
        "Enter Noise Pollution Complaint",
        placeholder="Example: Heavy traffic noise near Anna Nagar College Road at 8 PM. The noise level is around 82 dB."
    )

    if st.button("Analyze Complaint"):
        if complaint.strip() == "":
            st.warning("Please enter a noise complaint.")
        else:
            db_match = re.search(r"(\d{2,3})\s*(db|dB)", complaint)

            if db_match:
                noise_level = int(db_match.group(1))
            else:
                noise_level = 60

            sources = [
                "traffic",
                "construction",
                "vehicle horn",
                "horn",
                "loudspeaker",
                "factory",
                "crowd",
                "music"
            ]

            detected_source = "Not Mentioned"

            for source in sources:
                if source in complaint.lower():
                    detected_source = source.title()
                    break

            prompt = f"""
You are an AI Noise Pollution Assistant.

Analyze the following noise pollution complaint.

User Complaint:
{complaint}

Noise Level Detected: {noise_level} dB
Noise Source Detected: {detected_source}

Rules:
- Below 40 dB: Excellent Study Zone
- 40 to 55 dB: Good Study Zone
- 56 to 70 dB: Moderate Noise Zone
- Above 70 dB: Not Suitable for Studying

Return:
1. Risk Level
2. Study-Zone Status
3. Short Summary
4. Recommendation
"""

            if noise_level < 40:
                risk = "Low"
                status = "Excellent Study Zone"
                recommendation = "This location is peaceful and highly suitable for studying."
            elif noise_level <= 55:
                risk = "Low to Moderate"
                status = "Good Study Zone"
                recommendation = "This location is suitable for studying with minimal disturbance."
            elif noise_level <= 70:
                risk = "Moderate"
                status = "Moderate Noise Zone"
                recommendation = "Use headphones or choose a quieter indoor place such as a library."
            else:
                risk = "High"
                status = "Not Suitable for Studying"
                recommendation = "Avoid studying here during noisy hours. Use a library or quiet classroom."

            st.success("Analysis Completed!")

            st.subheader("Prompt Used in the Project")
            st.code(prompt, language="text")

            st.subheader("AI Analysis Result")

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**Detected Noise Source:** {detected_source}")
                st.write(f"**Detected Noise Level:** {noise_level} dB")

            with col2:
                st.write(f"**Risk Level:** {risk}")
                st.write(f"**Study-Zone Status:** {status}")

            st.subheader("Summary")
            st.info(
                f"The complaint reports {detected_source.lower()} noise "
                f"with an estimated noise level of {noise_level} dB."
            )

            st.subheader("Recommendation")
            st.warning(recommendation)

elif page == "Study-Zone Finder":
    st.title("📚 Study-Zone Finder")

    noise_level = st.slider(
        "Select Noise Level in dB",
        min_value=20,
        max_value=120,
        value=50
    )

    if noise_level < 40:
        st.success("Excellent Study Zone! 🌿")
        st.write("This area is very quiet and suitable for studying.")
    elif noise_level <= 55:
        st.info("Good Study Zone! 📖")
        st.write("This area is suitable for studying.")
    elif noise_level <= 70:
        st.warning("Moderate Noise Zone ⚠️")
        st.write("Use headphones or choose a quieter location.")
    else:
        st.error("Not Suitable for Studying! 🚫")
        st.write("This area has high noise pollution.")

elif page == "About Project":
    st.title("ℹ️ About This Project")

    st.write("""
    This project is developed using Python and Streamlit.

    The main AI component used is Prompt Engineering. The system creates a
    structured prompt containing the user complaint, noise-level rules, and
    expected output format.

    The prompt can later be connected to an AI model such as IBM Granite
    for real-time AI responses.
    """)

    st.subheader("Technologies Used")
    st.write("""
    - Python
    - Streamlit
    - Prompt Engineering
    - Regular Expressions
    """)
    