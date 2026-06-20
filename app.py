import streamlit as st
import pandas as pd
import numpy as np
import time
import hashlib

# Page configurations
st.set_page_config(page_title="Geldium AI Collections Dashboard", layout="wide", page_icon="🛡️")

# Styling adjustments
st.markdown("""
    <style>
    .main { background-color: #F8FAFC; }
    .risk-low { color: #10B981; font-weight: bold; }
    .risk-medium { color: #F59E0B; font-weight: bold; }
    .risk-high { color: #EF4444; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Geldium AI-Powered Collections Optimization Engine")
st.subheader("Autonomous Execution Platform with Responsible AI Guardrails")

# Sidebar - Security & Monitoring
st.sidebar.header("🔐 Security & Compliance Panel")
st.sidebar.info("DPDP Act 2023 & GDPR Compliance Status: ACTIVE")
anonymize_flag = st.sidebar.toggle("Real-Time PII Anonymization Tokenizer", value=True)
explain_mode = st.sidebar.checkbox("Show Model Explainability Logs (SHAP Vectors)", value=True)

# Dummy Dataset Creation
def load_mock_data():
    data = {
        "Customer_ID": ["CUST_9822", "CUST_4102", "CUST_7741", "CUST_3019", "CUST_8842"],
        "Outstanding_Amount (INR)": [45000, 120000, 15000, 85000, 210000],
        "DTI_Ratio": [0.35, 0.58, 0.22, 0.47, 0.65],
        "Repayment_Velocity_Score": [82, 41, 95, 63, 18],
        "Vulnerability_NLP_Index": [0.12, 0.05, 0.02, 0.85, 0.42] # High score = stressed text/voice metrics
    }
    return pd.DataFrame(data)

df = load_mock_data()

# Process PII Tokenization for Cyber Security tracking if enabled
if anonymize_flag:
    df["Customer_ID"] = df["Customer_ID"].apply(lambda x: "HASH_" + hashlib.md5(x.encode()).hexdigest()[:8].upper())

st.write("### 📊 Active Delinquent Account Portfolio View")
st.dataframe(df, use_container_width=True)

# Select Account for Simulation
st.write("---")
st.write("### ⚙️ Live Account Threat & Strategy Simulator")
selected_index = st.selectbox("Select Target Account Portfolio to evaluate Agentic Actions:", range(len(df)))

selected_row = df.iloc[selected_index]

# Core Logic Implementation
st.write(f"**Analyzing Account Vector:** `{selected_row['Customer_ID']}`")

# Algorithmic Scoring Calculations
risk_score = int((100 - selected_row["Repayment_Velocity_Score"]) * 0.7 + (selected_row["DTI_Ratio"] * 100) * 0.3)

# Display Risk Categorization
if risk_score < 40:
    st.markdown(f"**Computed Portfolio Risk Category:** <span class='risk-low'>LOW RISK ({risk_score}%)</span>", unsafe_allow_html=True)
    suggested_action = "Deploy Fully Autonomous Early WhatsApp Nudges & Payment Token Setup"
    autonomy_level = "FULLY AUTONOMOUS (Agent Controlled)"
elif risk_score < 70:
    st.markdown(f"**Computed Portfolio Risk Category:** <span class='risk-medium'>MEDIUM RISK ({risk_score}%)</span>", unsafe_allow_html=True)
    suggested_action = "Trigger Interactive Multilingual AI Voicebot Negotiation Flow"
    autonomy_level = "SEMI-AUTONOMOUS (Agent Triggered / Human Override)"
else:
    st.markdown(f"**Computed Portfolio Risk Category:** <span class='risk-high'>HIGH RISK ({risk_score}%)</span>", unsafe_allow_html=True)
    suggested_action = "Escalate to Premium Hardship Underwriter for Restructuring Terms"
    autonomy_level = "HUMAN-IN-THE-LOOP MANDATORY"

# Vulnerability Overriding Check (Ethical/Responsible AI Component)
if selected_row["Vulnerability_NLP_Index"] > 0.60:
    st.warning("⚠️ **Vulnerability Sentiment Flag Triggered!** Sentiment detection algorithms identified financial distress patterns or extreme stress markers in recent communication logs.")
    suggested_action = "🚨 CRITICAL OVERRIDE: Immediately suspend automated robotic outbox loops. Route collection ownership to the Ethical Resolution Desk Agent."
    autonomy_level = "HUMAN INTERVENTION COMPULSORY"

# Render Action Frame
st.info(f"🎯 **Recommended Action Protocol:** {suggested_action}")
st.success(f"🤖 **Operational Autonomy Clearance:** {autonomy_level}")

# Model Explainability Feature
if explain_mode:
    st.write("#### 🔍 Structural Model Feature Weights (SHAP Values)")
    feature_importance = pd.DataFrame({
        'Feature Parameter': ['Repayment Velocity Track', 'Debt-to-Income Weights', 'Behavioral Contact Flags'],
        'Impact Metric': [0.55 if risk_score > 50 else 0.70, 0.35, 0.10]
    })
    st.bar_chart(feature_importance.set_index('Feature Parameter'))

# Simulate Action Deployment
if st.button("🚀 Deploy Strategy & Log Event"):
    with st.spinner("Processing token distributions and logging compliance metrics..."):
        time.sleep(1.5)
        st.balloons()
        st.success("Strategy executed successfully! Compliance payload recorded inside distributed transaction logging vaults.")