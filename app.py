import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

st.set_page_config(page_title="Eloquence Engine 2.0", page_icon="🎙️")

# --- APP HEADER ---
st.title("🎙️ Eloquence Engine 2.0")
st.markdown("### From Clarity to Charisma: Your Daily Stage-Ready System")

# --- SIDEBAR: NAVIGATION & PROGRESS ---
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Go To:", ["Daily Training", "Charisma Mastery Vault", "Stage Readiness Tracker"])

# --- CHARISMA DATA ---
charisma_keys = {
    "1. First Impression Hacks": "The 'Eyebrow Flash' & 2-Second Smile. Use open palms to show you aren't a threat.",
    "2. Build Trust with Voice": "End your sentences with a *descending* inflection. It makes you sound authoritative.",
    "3. Confidence Wins": "Slow down your speech by 10%. Silence is a power move, not a mistake.",
    "4. Speak Up in Any Room": "The 'First 5 Rule': Make a comment within the first 5 mins of a meeting to establish presence.",
    "5. Storytelling Secrets": "Use the 'Vulnerability Loop': Share a small mistake, then how you solved it.",
    "6. Body Language": "Power Posing: Hands on hips, feet wide. Hold for 2 mins before a call to boost testosterone.",
    "7. Read People Like a Pro": "Look for 'Blocking': If someone crosses their arms or legs, they are losing interest.",
    "8. Give Tough Feedback Fast": "Use the 'I feel...' method. 'I feel concerned about the timeline,' instead of 'You are late.'",
    "9. Handle Difficult People": "The 'Fogging' Technique: Agree with any truth in their criticism to de-arm them.",
    "10. Say NO & Be Likable": "The 'Positive No': 'I'd love to help, but my current focus is on [X] right now.'",
    "11. Interrupt Smoothly": "The 'Ledge': Wait for a breath, say 'That's a great point, and building on that...'",
    "12. Defuse Any Conflict": "Lower your volume. When they get loud, you get quieter. It forces them to listen.",
    "13. Listen Like a Leader": "Reflective Listening: 'So what I’m hearing is...' It builds instant deep rapport.",
    "14. Small Talk Magic": "Use the F.O.R.D. Method: Ask about Family, Occupation, Recreation, or Dreams."
}

# --- PAGE 1: DAILY TRAINING ---
if menu == "Daily Training":
    with st.expander("✨ Step 1: Pac-Man Grounding (4-7-8)", expanded=False):
        if st.button("🚀 Start 1-Minute Grounding"):
            placeholder = st.empty()
            for cycle in range(3):
                for i in range(1, 5): # Inhale
                    placeholder.markdown(f"### 😤 Inhale... \n # 👄 {'· ' * (4-i)} 🍕")
                    time.sleep(1)
                for i in range(1, 8): # Hold
                    placeholder.markdown(f"### ✋ Hold... \n # 👄 🍕")
                    time.sleep(1)
                for i in range(1, 9): # Exhale
                    placeholder.markdown(f"### 🌬️ Exhale... \n # {'&nbsp; ' * (i*2)} 👄 💨")
                    time.sleep(1)
            placeholder.success("Grounded.")

    tab1, tab2, tab3, tab4 = st.tabs(["Read", "Drills", "Vocab", "Record"])
    with tab1:
        st.write("Read slowly. Focus on the 'D' and 'T' endings.")
        st.info("'The world belongs to those who can articulate their vision with clarity and conviction.'")
    with tab2:
        st.warning("1. Red Leather, Yellow Leather\n2. Unique New York\n3. Toy boat, toy boat, toy boat")
    with tab3:
        st.success("**Eloquent** (fluent/persuasive) | **Resilient** (quick recovery) | **Strategic** (long-term plan)")
    with tab4:
        audio = mic_recorder(start_prompt="Record 3-5 Mins Practice", stop_prompt="Stop & Analyze", key='rec')
        if audio: st.audio(audio['bytes'])

# --- PAGE 2: CHARISMA VAULT ---
elif menu == "Charisma Mastery Vault":
    st.header("The 14 Keys to Charisma")
    choice = st.selectbox("Pick a skill to master today:", list(charisma_keys.keys()))
    
    st.markdown(f"### 💡 The Strategy")
    st.info(charisma_keys[choice])
    
    st.markdown("### 🛠️ Practice Challenge")
    st.write(f"Today, find one opportunity to use this **{choice}** technique.")
    if st.button("Mark as Practiced Today"):
        st.balloons()

# --- PAGE 3: TRACKER ---
elif menu == "Stage Readiness Tracker":
    st.header("Your Journey to the Stage")
    days = st.slider("Days Completed", 0, 100, 1)
    st.progress(days/100)
    if days > 10: st.write("✅ Speech 'Blur' is fading.")
    if days > 30: st.write("✅ Confidence in client meetings is rising.")
    if days > 90: st.write("🚀 READY FOR THE PODCAST/STAGE.")
