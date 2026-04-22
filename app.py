import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

st.set_page_config(page_title="Eloquence Engine", page_icon="🎙️")

# --- PART 8 & 1: STABILIZE & GROUNDING (The Therapy Layer) ---
st.title("🎙️ Eloquence Engine")
with st.expander("✨ Step 1: Ground Your Nervous System", expanded=True):
    st.write("Before you speak, you must be calm. Follow the prompt below:")
    st.info("Inhale for 4 seconds... Hold for 7... Exhale for 8.")
    if st.button("Start 1-Minute Grounding Timer"):
        progress_bar = st.progress(0)
        for i in range(60):
            time.sleep(1)
            progress_bar.progress((i + 1) / 60)
        st.success("You are grounded. Your voice is ready.")

# --- THE 30-MINUTE DAILY TRAINING (Part 10) ---
st.divider()
st.header("Today's Training")

tab1, tab2, tab3, tab4 = st.tabs(["1. Read (10m)", "2. Drills (5m)", "3. Vocab (5m)", "4. Record (10m)"])

with tab1:
    st.subheader("Slow Reading")
    st.write("Read the following paragraph out loud. Move your mouth *excessively*.")
    st.info("""'The articulate architect achieved an amazing advantage by 
    addressing the audience with absolute authenticity.'""")
    st.caption("Focus on the 'T' and 'K' sounds at the ends of words.")

with tab2:
    st.subheader("Enunciation Drills")
    st.write("Repeat these 5 times each, faster every time:")
    st.warning("1. Red Leather, Yellow Leather\n\n2. Six slippery snails slid slowly\n\n3. Truly rural")

with tab3:
    st.subheader("Vocabulary: The 'Client' Words")
    st.write("Try to use these 3 words in your recording next:")
    st.success("**Pivot** (to change direction) | **Leverage** (to use effectively) | **Holistic** (considering the whole)")

# --- PART 3: RECORD & PLAYBACK ---
with tab4:
    st.subheader("Record & Playback")
    st.write("Explain your goal of doing a TED talk one day. Use your 3 new vocab words.")
    
    # This creates a real record button and playback UI
    audio = mic_recorder(
        start_prompt="Click to Start Recording",
        stop_prompt="Click to Stop & Listen",
        key='recorder'
    )

    if audio:
        st.audio(audio['bytes'])
        st.download_button("Download My Speech", audio['bytes'], file_name="my_practice.wav")
        st.write("---")
        st.write("**Self-Correction Checklist:**")
        st.checkbox("Did I mumble any endings?")
        st.checkbox("Did I breathe between sentences?")
        st.checkbox("Did I sound like I believe what I'm saying?")

# --- PART 9: PROGRESS TRACKING ---
st.sidebar.header("Your Progress")
days = st.sidebar.slider("Days Completed", 0, 30, 1)
st.sidebar.write(f"You are {int((days/30)*100)}% of the way to your Stage Goal!")
