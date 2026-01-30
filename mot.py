import streamlit as st
import os
import random

# ================= Page Config =================
st.set_page_config(page_title="Just For You ❤️", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0b0b0d, #141418);
    color: #e5e5ea;
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
    margin:0;
    padding:0;
}

/* Cards */
.card {
    background: rgba(20, 20, 24, 0.9);
    border-radius: 25px;
    padding: 50px 30px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
    text-align: center;
    margin: 40px auto;
    max-width: 850px;
}

h1 {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    color: #f5f5f7;
    margin-bottom: 20px;
}

p {
    margin-bottom: 20px;
}

/* Button */
.btn {
    background: linear-gradient(135deg, #2b2b30, #3a3a42);
    color: #f5f5f7;
    border: none;
    padding: 14px 28px;
    font-size: 1rem;
    border-radius: 50px;
    cursor: pointer;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 30px rgba(255, 255, 255, 0.15);
}

/* Collage */
.collage {
    display: flex;
    gap: 10px;
    overflow: hidden;
    margin-top: 20px;
}
.collage-track {
    display: flex;
    animation: scrollCollage 15s linear infinite;
}
.collage img {
    width: 120px;
    height: 120px;
    object-fit: cover;
    border-radius: 15px;
    border: 2px solid #e5e5ea;
    box-shadow: 0 5px 15px rgba(255,255,255,0.1);
}
@keyframes scrollCollage {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}

/* Floating flowers */
.floating-flower {
    position: fixed;
    bottom: -80px;
    z-index: 3;
    pointer-events: none;
    filter: drop-shadow(0 0 6px rgba(255, 200, 220, 0.6));
    animation: floatUp linear forwards;
}
@keyframes floatUp {
    0% { transform: translateY(0); opacity:1; }
    100% { transform: translateY(-120vh); opacity:0; }
}
</style>
""", unsafe_allow_html=True)

# ================= IMAGE SETUP =================
IMAGE_FOLDER = "IMAGES"
images = [os.path.join(IMAGE_FOLDER, f"{i}.jpeg") for i in range(1, 25)]

# ================= Session State =================
if 'step' not in st.session_state:
    st.session_state.step = 1

# ================= Helper Functions =================
def display_collage(img_list):
    st.markdown('<div class="collage"><div class="collage-track">', unsafe_allow_html=True)
    for img in img_list:
        st.markdown(f'<img src="{img}" />', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

def show_flowers():
    for _ in range(40):
        flower = random.choice(['🌸','🌺','🌹'])
        left = random.randint(0, 100)
        size = round(random.uniform(3.5, 6), 1)
        duration = round(random.uniform(8, 18), 1)
        delay = round(random.uniform(0, 4), 1)
        st.markdown(f"""
        <div class="floating-flower" style="
            left:{left}vw;
            font-size:{size}rem;
            animation-duration:{duration}s;
            animation-delay:{delay}s;">
            {flower}
        </div>
        """, unsafe_allow_html=True)

# ================= APP LOGIC =================
# Step 1
if st.session_state.step == 1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h1>Hey Lab 💌</h1>', unsafe_allow_html=True)
    st.markdown('<p>I made something just for you…</p>', unsafe_allow_html=True)
    if st.button("Tap to open your surprise ✨"):
        st.session_state.step = 2
    st.markdown('</div>', unsafe_allow_html=True)

# Step 2
elif st.session_state.step == 2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h1>Happy Monthsary ❤️</h1>', unsafe_allow_html=True)
    st.markdown('<p>Just a short message before the surprise…</p>', unsafe_allow_html=True)
    if st.button("Read it 💗"):
        st.session_state.step = 3
    st.markdown('</div>', unsafe_allow_html=True)

# Step 3
elif st.session_state.step == 3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p>Every month with you is something I’m grateful for. Thank you for being my safe place, my comfort, and my favorite person. I’m excited for all the days we still get to share.</p>', unsafe_allow_html=True)
    display_collage(images)
    if st.button("Flower for you!!!! 🌸"):
        st.session_state.step = 4
    st.markdown('</div>', unsafe_allow_html=True)

# Step 4 (floating flowers visible)
elif st.session_state.step == 4:
    show_flowers()
