import streamlit as st
import random

# Set up page config with custom background
st.set_page_config(page_title="MoodMatrix AI", layout="centered", page_icon="🧠")

# Custom CSS for vibrant colors and animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

:root {
    --primary: #6a11cb;
    --secondary: #2575fc;
    --accent: #ff4d4d;
    --light: #f8f9fa;
}

body {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
    animation: gradient 15s ease infinite;
    background-size: 400% 400%;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stTextInput>div>div>input {
    color: #333 !important;
    background-color: rgba(255,255,255,0.9) !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

.content-card {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 16px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    transition: transform 0.3s ease;
}

.content-card:hover {
    transform: translateY(-5px);
}

.emoji-header {
    font-size: 3rem;
    text-align: center;
    margin-bottom: 0.5rem;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.stButton>button {
    background: linear-gradient(45deg, #ff4d4d, #f9cb28);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 24px;
    font-weight: 600;
    box-shadow: 0 4px 14px rgba(255,77,77,0.4);
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(255,77,77,0.6);
}

.header-container {
    background: rgba(0,0,0,0.2);
    padding: 2rem;
    border-radius: 16px;
    margin-bottom: 2rem;
    text-align: center;
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255,255,255,0.3);
}

/* Mood-specific animations */
.happy-effect {
    animation: happyPulse 1s ease infinite;
}

@keyframes happyPulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
}

.sad-effect {
    animation: sadFloat 3s ease-in-out infinite;
}

@keyframes sadFloat {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

.anxious-effect {
    animation: shake 0.5s ease-in-out infinite;
}

@keyframes shake {
    0% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
    100% { transform: translateX(0); }
}

.bored-effect {
    animation: spin 2s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.romantic-effect {
    animation: heartbeat 1.5s ease infinite;
}

@keyframes heartbeat {
    0% { transform: scale(1); }
    25% { transform: scale(1.1); }
    50% { transform: scale(1); }
    75% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

# Define possible AI-generated content types with more variety
content_types = {
    "happy": [
        {"type": "🎤 Stand-up Comedy", "content": "The AI brings you a 5-minute act titled 'Life with Indian Moms'", "color": "#FF9E7D"},
        {"type": "🎶 Uplifting Music", "content": "Synthwave + Bollywood fusion to make your heart dance", "color": "#7DBEFF"},
        {"type": "📖 Story", "content": "A chaiwala wins a reality show and mentors start-up kids", "color": "#A0E7A0"},
        {"type": "🎭 Skit", "content": "Two ghosts fighting over a haunted mansion's Instagram handle", "color": "#FFB6D9"}
    ],
    "sad": [
        {"type": "🎵 Lo-fi Rainy Vibes", "content": "Sounds of a Kolkata tram with gentle guitar strums", "color": "#7D8AFF"},
        {"type": "🎙️ Podcast", "content": "The Psychology of Letting Go - A therapist talks healing", "color": "#A0E7E5"},
        {"type": "📖 Story", "content": "A long-lost friend sends a postcard from Himachal", "color": "#FFD47D"},
        {"type": "🎭 Audio Play", "content": "A dog waits by the door - based on a true story", "color": "#D9A0FF"}
    ],
    "anxious": [
        {"type": "🎶 Meditation Tones", "content": "Tibetan bowls and binaural beats for grounding", "color": "#A0E7A0"},
        {"type": "🎙️ Mini Podcast", "content": "AI walks you through a 4-7-8 breathing cycle", "color": "#7D8AFF"},
        {"type": "📖 Story", "content": "An introvert becomes a TED speaker thanks to his cat", "color": "#FFB6D9"},
        {"type": "🧘 Guided Visualization", "content": "Imagine floating over Kerala backwaters at sunrise", "color": "#FF9E7D"}
    ],
    "bored": [
        {"type": "🎤 Roast Byte", "content": "AI roasts your name, crush & zodiac sign 🤭", "color": "#FF4D4D"},
        {"type": "📻 Rapid-Fire Trivia", "content": "5 quirky facts in 30 seconds!", "color": "#F9CB28"},
        {"type": "📖 Story", "content": "A failed heist planned on a Goa beach by drunk poets", "color": "#7DBEFF"},
        {"type": "🎮 Interactive Game", "content": "Solve a riddle with sound clues", "color": "#A0E7E5"}
    ],
    "romantic": [
        {"type": "🎶 Custom Song", "content": "Bollywood violin meets modern ballad love loop", "color": "#FFB6D9"},
        {"type": "📖 Story", "content": "A metro delay leads to a meet-cute between commuters", "color": "#FF9E7D"},
        {"type": "🎙️ Podcast", "content": "Real voices share first kiss stories anonymously", "color": "#7D8AFF"},
        {"type": "💌 Audio Letter", "content": "AI-generated message from a fictional lover", "color": "#D9A0FF"}
    ]
}

# Mood effect mapping
mood_effects = {
    "happy": "happy-effect",
    "sad": "sad-effect",
    "anxious": "anxious-effect",
    "bored": "bored-effect",
    "romantic": "romantic-effect"
}

# Custom header
st.markdown("""
<div class="header-container">
    <h1 style='color: white; margin-bottom: 0.5rem;'>🧠 MoodMatrix AI</h1>
    <h3 style='color: white; margin-top: 0;'>One Input, Infinite Audio Experiences</h3>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="emoji-header">🎧</div>', unsafe_allow_html=True)
st.markdown("""
<h3 style='text-align: center; color: white; margin-bottom: 2rem;'>
Describe your mood, and let generative AI flood your ears with perfect vibes
</h3>
""", unsafe_allow_html=True)

# Mood input with styled container
mood_input = st.text_input(
    "🎙️ How are you feeling today?",
    placeholder="Try: happy, sad, anxious, bored, romantic...",
    key="mood_input_field"
)

# Add voice input suggestion
st.markdown("""
<p style='color: white; text-align: center; font-size: 0.9rem;'>
<i>Tip: Tap the mic icon on your keyboard for voice input!</i>
</p>
""", unsafe_allow_html=True)

# Mood processing
if mood_input:
    mood = mood_input.strip().lower()
    
    if mood in content_types:
        # Success message with mood-specific animation
        with st.spinner('✨ Cooking up your perfect audio mix...'):
            # Apply mood-specific effect
            effect_class = mood_effects.get(mood, "")
            st.markdown(f'<div class="{effect_class}" style="text-align: center; font-size: 3rem;">🎧</div>', unsafe_allow_html=True)
            
            # Mood-specific success message
            success_messages = {
                "happy": "Let's turn that smile into a laugh!",
                "sad": "We'll help you through this...",
                "anxious": "Take a deep breath with us...",
                "bored": "Let's spice things up!",
                "romantic": "Love is in the air..."
            }
            st.success(f"**{success_messages.get(mood, 'Here are your AI-curated experiences')}**")
        
        # Display content cards
        outputs = random.sample(content_types[mood], 3)
        
        for item in outputs:
            st.markdown(f"""
            <div class="content-card" style="border-left: 6px solid {item['color']};">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="font-size: 2rem;">{item['type'].split()[0]}</div>
                    <div>
                        <h4 style="margin-bottom: 0.5rem; color: {item['color']}">{item['type']}</h4>
                        <p>{item['content']}</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Add play button
            if st.button(f"▶️ Play {item['type'].split()[0]}", key=f"play_{item['type']}"):
                st.toast(f"Now playing: {item['type']}")
                
        # Refresh button
        if st.button("🔄 Mix it up!", type="primary"):
            st.experimental_rerun()
            
    else:
        # Playful error message
        st.error("""
        Oops! My AI doesn't understand that mood yet. 
        Try one of these: happy, sad, anxious, bored, or romantic.
        """)
        
        # Mood suggestion chips
        cols = st.columns(5)
        for i, suggested_mood in enumerate(["happy", "sad", "anxious", "bored", "romantic"]):
            with cols[i]:
                if st.button(suggested_mood.capitalize(), key=f"suggest_{suggested_mood}"):
                    st.session_state.mood_input_field = suggested_mood
                    st.experimental_rerun()

# Footer
st.markdown("""
<div style='text-align: center; color: white; margin-top: 3rem;'>
    <p>Made with ❤️ for Kuku FM</p>
    <p>Try saying: "excited", "nostalgic", or "adventurous"</p>
</div>
""", unsafe_allow_html=True)
