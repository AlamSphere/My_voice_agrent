# My_voice_agrent
Production-ready, low-latency AI Voice Agent built with ElevenLabs Conversational AI, Python, and Streamlit. Features real-time WebSocket audio streaming, custom career persona prompts, and a live web demo interface.
# 🎙️ AI Voice Agent & Portfolio Assistant

[![Live Demo](https://img.shields.io/badge/Live%20Demo-GitHub%20Pages-blue?style=for-the-badge&logo=github)](https://YOUR_GITHUB_USERNAME.github.io/ai-voice-agent/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blueviolet?style=for-the-badge&logo=python)](https://www.python.org/)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-Conversational%20AI-orange?style=for-the-badge)](https://elevenlabs.io/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Control%20Center-red?style=for-the-badge&logo=streamlit)](https://streamlit.io/)

A production-grade, low-latency Conversational AI voice agent engineered to act as an automated career representative and portfolio assistant. This project demonstrates real-time bidirectional WebSocket audio streaming, custom prompt alignment based on technical resumes, and a decoupled client-server architecture.

---

## 🚀 Key Features

* **Real-Time Voice Streaming:** Powered by ElevenLabs Conversational AI SDK for ultra-low latency (<400ms) neural text-to-speech and speech-to-text.
* **Custom Career Persona:** Programmed with a detailed system prompt mirroring professional achievements, machine learning research publications (CNN crowd counting with 92% accuracy)[cite: 1], and full-stack RAG projects.
* **Interactive Control Center:** Built with **Streamlit** to manage session parameters, view telemetry, and log live conversation transcripts.
* **Web-Based Embed Widget:** Deployed as a static portfolio page via **GitHub Pages** allowing recruiters to talk directly with the agent straight from their browser.

---

## 🛠️ Tech Stack

* **Backend / Core Engine:** Python, `elevenlabs`, `python-dotenv`
* **UI / Dashboards:** Streamlit, HTML5 / JavaScript Embed Widget
* **Networking / Transport:** Secure WebSockets (`WSS`)
* **Deployment:** GitHub Pages (Frontend), Local Environment (Python Orchestration)

---

## 📂 Project Structure

```text
ai-voice-agent/
│
├── src/
│   ├── agent.py         # Core Python WebSocket voice session loop
│   └── app.py           # Streamlit control center dashboard
│
├── index.html           # Public portfolio landing page with voice widget
├── requirements.txt     # Python project dependencies
├── .env.example         # Template for environment variables
└── README.md            # Project documentation
