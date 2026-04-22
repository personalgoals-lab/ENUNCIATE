import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

st.set_page_config(page_title="Eloquence Engine", page_icon="🎙️")

# --- APP HEADER ---
st.title("🎙️ Eloquence Engine")
st.markdown("""
**Your Daily Voice Architect.** This app is designed to help you transition from 'blurry' speech to stage-ready confidence. 
By combining grounding therapy, physical enunciation drills, and real-time feedback, 
we are rebuilding your communication muscles for your future clients and that TED stage.
""")

# --- STEP 1: STABILIZE & GROUNDING (The Pac-Man Therapy Layer) ---
st.divider()
with st.expander("✨ Step 1: Ground Your Nervous System", expanded=True):
    st.write("Follow the Pac-Man to stabilize your breath (4-7-8 Technique).")
    
    if st.button("🚀 Start 1-Minute Grounding"):
        placeholder = st.empty()
        timer_text = st.empty()
        
        # Total 1 minute is roughly 3 full cycles of 4-7-8
        for cycle in range(3):
            # 1. INHALE (4 seconds) - Pac-Man "Eating"
            for i in range(1, 5):
                dots = "· " * (4 - i)
                placeholder.markdown(f"### 😤 Inhale... \n # 👄 {dots} 🍕")
                timer_text.write(f"Seconds: {i}")
                time.sleep(1)
            
            # 2. HOLD (7 seconds) - Pac-Man Staying Still
            for i in range(1, 8):
                placeholder.markdown(f"### ✋ Hold... \n # 👄 🍕")
                timer_text.write(f"Seconds: {i}")
                time.sleep(1)
                
            # 3. EXHALE (8 seconds) - Pac-Man Walking Out
            for i in range(1, 9):
                spaces = "&nbsp; " * (i * 2)
                placeholder.markdown(f"### 🌬️ Exhale... \n # {spaces} 👄 💨")
                timer_text.write(f"Seconds: {i}")
                time.sleep(1)
        
        placeholder.success("🎉 Grounding Complete. You are focused and ready to speak.")
        timer_text.empty()

# --- THE 30-MINUTE DAILY TRAINING ---
st.header("Today's Training Circuit")
tab1, tab2, tab3, tab4 = st.tabs(["1. Read (10m)", "2. Drills (5m)", "3. Vocab (5m)", "4. Record (10m)"])

with tab1:
    st.subheader("Slow Reading")
    st.write("Read this aloud. Over-articulate every single syllable.")
    st.info("""'Precision in speech is the precursor to professional power. 
    When we articulate clearly, we command the room and instill confidence 
    in our clients and ourselves.'""")

with tab2:
    st.subheader("Enunciation Drills")
    st.write("Repeat these 5 times each. Feel your facial muscles working!")
    st.warning("1. Red Leather, Yellow Leather\n\n2. The specific skeptic speaks specifically.\n\n3. Proper copper coffee pot.")

with tab3:
    st.subheader("Vocabulary Expansion")
    st.write("Incorporate these into your recording next:")
    st.success("**Synchronicity** (happening at the same time) | **Scalable** (able to grow) | **Concise** (brief but comprehensive)")

with tab4:
    st.subheader("Record & Playback")
    st.write("Simulation: *A client asks you, 'What is your vision for your career in 3 years?'*")
    
    audio = mic_recorder(
        start_prompt="Click to Start Recording",
        stop_prompt="Click to Stop & Listen",
        key='recorder'
    )

    if audio:
        st.audio(audio['bytes'])
        st.write("**Self-Reflection:** Did you use your new vocabulary? Was your voice 'blurry' or 'bright'?")

# --- PROGRESS TRACKING ---
st.sidebar.header("Stage Readiness")
progress = st.sidebar.slider("Days Active", 0, 30, 5)
st.sidebar.progress(progress * 3.33 / 100)
st.sidebar.write(f"Current Level: {'Newcomer' if progress < 10 else 'Rising Speaker'}")
