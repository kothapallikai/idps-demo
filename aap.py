import streamlit as st
import pandas as pd
import random

st.title("AI-Powered Quantum Secure Automotive IDPS Demo")

# Simulated CAN Bus Data
can_data = pd.DataFrame([
    {"ID": 100, "Speed": 40, "RPM": 2000, "Status": "Normal"},
    {"ID": 101, "Speed": 50, "RPM": 2500, "Status": "Normal"},
    {"ID": 102, "Speed": 0, "RPM": 0, "Status": "Spoofing Detected"},
    {"ID": 103, "Speed": 120, "RPM": 6000, "Status": "DoS Attack Detected"},
])

st.subheader("Real-Time Vehicle CAN Bus Data")
st.dataframe(can_data)

# AI-Based Intrusion Detection Simulation
if st.button("Run AI-Based Intrusion Detection"):
    attack_type = random.choice(["Normal", "Spoofing", "DoS", "Malware"])
    if attack_type != "Normal":
        st.warning(f"Intrusion Detected: {attack_type}")
    else:
        st.success("No intrusion detected.")

# Quantum Key Generation Simulation
if st.button("Generate Quantum Key"):
    quantum_key = random.randint(100000, 999999)
    st.success(f"Quantum Key Generated: {quantum_key}")

# OTA Security Patch Deployment Simulation
if st.button("Deploy OTA Security Patch"):
    st.info("Deploying OTA Update...")
    st.success("Vehicle firmware successfully secured!")
