import streamlit as st
import time

st.set_page_config(page_title="Eloquence Engine", layout="centered")

st.title("🎙️ The Eloquence Engine")
st.subheader("Daily Communication Training")

# --- Progress Tracking (Mock Data) ---
def show_progress():
    st.sidebar.header("Your Progress")
    st.sidebar.progress(70) # Example 70%
    st.sidebar.write("🔥 5 Day Streak")
    st.sidebar.write("📊 Clarity Score: 8.5/10")

show_progress()

# --- Part 1: Grounding (Therapy Layer) ---
with st.expander("Step 1: Grounding & Stabilization (2 Mins)", expanded=True):
    st.info("Follow the circle: Inhale as it grows, Exhale as it shrinks.")
    st.write("Focus on the physical sensation of your feet on the floor.")

# --- Part 2: The 30-Minute Daily Circuit ---
tab1, tab2, tab3, tab4 = st.tabs(["Read Aloud", "Enunciation", "Vocabulary", "Record"])

with tab1:
    st.header("10 Mins: Slow Reading")
    st.write("**Topic of the Day:** *The Future of Client Relations*")
    st.markdown("""
    > "Confidence is not the absence of fear, but the mastery of it. 
    > When we speak to clients, we are not just delivering data; 
    > we are delivering a sense of security and expertise."
    """)
    st.caption("Read this 3 times: Once fast, once slow, once with 'chewing' movements.")

with tab2:
    st.header("5 Mins: Enunciation Drills")
    drills = [
        "The blue bluebird blinks at the bright breeze.",
        "Specific statistics suggest systemic success.",
        "Unique New York, You know you need New York."
    ]
    for drill in drills:
        st.button(drill)

with tab3:
    st.header("5 Mins: Vocabulary Expansion")
    st.table({
        "Word": ["Articulate", "Pragmatic", "Nuanced"],
        "Definition": ["Able to express ideas clearly", "Dealing with things sensibly", "Subtle shades of meaning"],
        "Client Context": ["'Let me articulate that solution...'", "'The pragmatic approach is...'", "'There is a nuanced difference...'"]
    })

with tab4:
    st.header("10 Mins: Record & Simulation")
    st.write("**Prompt:** Explain to a client why they should choose your service.")
    # In a real app, you'd use a recording component like streamlit-mic-recorder
    st.warning("Use your phone or local recorder for this 3-5 minute block.")
    if st.button("Start Playback Timer"):
        with st.empty():
            for i in range(300, 0, -1):
                st.write(f"Remaining: {i//60}:{i%60:02d}")
                time.sleep(1)
            st.success("Session Complete!")

# --- Stimulate Real Client Conversation ---
st.divider()
st.subheader("Client Simulation Challenge")
st.write("*Client: 'I'm worried this project is going to take too long. Why should I trust you?'*")
st.text_area("Draft your response using the PEEL method:")
