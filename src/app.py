import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Production Voice Agent Control Center",
    page_icon="🎙️",
    layout="wide"
)

# Custom Styling & Header
st.title("🎙️ Production Voice Agent Control Center")
st.markdown("Manage, monitor, and interact with your real-time ElevenLabs Conversational AI voice agent.")

#
# Main Dashboard Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔌 Session Management")
    st.info("System Ready. Use your local terminal to run the bi-directional microphone stream, or monitor active parameters here.")
    
    if st.button("🚀 Launch Terminal Script Reminder", type="primary"):
        st.code("python src/agent.py", language="bash")

with col2:
    st.subheader("📊 Real-Time Telemetry")
    st.metric(label="Target Latency", value="< 400 ms", delta="Optimal")
    st.metric(label="WebSocket Protocol", value="Secure (WSS)", delta="Active")

st.markdown("---")
st.subheader("📝 Live Conversation Logs & Transcripts")
st.text_area(
    "Transcript Stream", 
    placeholder="Session transcript logs will output here in real time during active calls...", 
    height=250
)