import requests
import streamlit as st
from pathlib import Path
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page


# --- GENERAL SETTINGS ---
favicon = "https://res.cloudinary.com/dvz16ceua/image/upload/v1692056331/sihem/favicon_q0aqzk.ico"
PAGE_TITLE = "CV | Sihem Ouled Hsin"

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title=PAGE_TITLE, page_icon=favicon, layout="wide")


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/9a04e479-2f4f-49ca-8979-2ec814eeb34b/vLfEcolLRX.json")
img_book = Image.open("assets/book.png") 
img_app = Image.open("assets/appSihem.png")
banner = "https://res.cloudinary.com/dvz16ceua/image/upload/v1692319771/sihem/sihem_hsin_yi6smh.png"
img_coach = Image.open("assets/coach.png")

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


# ---- MENU SECTION ----

# Sidebar content
with st.sidebar.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(favicon)
    with col2:
        st.markdown(
            """
            <div style="font-size: 16px; font-weight: bold; margin-top: 15px;">Main Menu</div>
            """
            , unsafe_allow_html=True)

# ---- Banner ----
st.markdown(
    f"""
    <style>
    .banner {{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 500px; /* Adjust the height as needed */
        background-image: url('{banner}');
        background-size: cover; /* Adjust background sizing */
        background-position: center;
        background-repeat: no-repeat; /* Prevent repeating the image */
        color: white; /* Text color on the banner */
    }}
    .banner-text {{
        margin-top: 10px; /* Add some margin below the image */
    }}

    /* Media query for smaller screens (max-width: 600px) */
    @media (max-width: 600px) {{
        .banner {{
            height: 200px; /* Adjust height for mobile */
        }}
    }}
    </style>
    <div class="banner">
    
    </div>
    """,
    unsafe_allow_html=True
)



# ---- HEADER SECTION ----
with st.container():
    st.title("Developer - P O R T F O L I O")
    

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.header("BIO")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        
        st.write("##")
        st.write(
            """
I'm a fervent advocate for the art of doing—constantly pushing boundaries, learning, and evolving. A true embodiment of a hard worker and a rapid learner, I have embarked on a journey of continuous exploration across numerous realms.

From my early forays into the medical field, where I passionately delved into the complexities of healthcare, to my later transition into the dynamic landscape of IT, I've exemplified adaptability and perseverance. I founded my own venture, a testament to my entrepreneurial spirit, despite the challenges.
My unwavering drive led me to challenge myself once more, re-entering the world of academia to emerge as a resolute developer in the realm of technology. This relentless commitment echoes my profound belief in self-evolution and transformation.

            """
        )
        
    with mid_column:
        st_lottie(lottie_coding, height=300, key="coding")
    with right_column:
        st.write("##")
        st.write(
            """

Beyond traditional boundaries, I've also ventured into the realms of coaching and writing, seizing every opportunity to broaden my horizons. My approach is simple: if there's a chance to learn, grow, or create, count me in. Every endeavor is a testament to my unyielding dedication and ceaseless pursuit of excellence.

In a world teeming with possibilities, I am a spirited and passionate individual who doesn't merely seize opportunities—I proactively carve them. Guided by the steadfast belief that life is a canvas awaiting strokes of brilliance, I am on an unending quest to not only find my passion but to create it, and to forge a legacy that embodies the resilience and determination that define me.
            """)
        st.write("##")
        button1=st.button(" 📑 Please find my cv here ... ")
        if button1:
            switch_page("cv")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("PROFILE")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_app)
    with text_column:
        st.subheader("Programming")
        st.write(
            """
            In my programming journey, I've embarked on various projects that reflect my dedication to mastering multiple languages. From diving into the intricacies of Python to harnessing the power of Java..., I've continually pushed my boundaries to create meaningful solutions. Each project has been an opportunity for me to showcase my best work, applying my knowledge and skills gained from rigorous study and immersive courses. Despite the progress I've made, I recognize that I'm still at the junior stage of my career. While I bring a solid foundation and enthusiasm to the table, I'm keenly aware that experience is the true catalyst for growth. I'm committed to gaining more hands-on experience to fully demonstrate my potential and contribute effectively to the world of software development."""
        )
        st.markdown("[See portfolio...](https://github.com/SihemOHsin?tab=repositories)")

with st.container():
    st.write("##")
    text_column, image_column = st.columns((2, 1))
    with image_column:
        st.image(img_book)
    with text_column:
        st.subheader("Writing")
        st.write(
            """
               I have authored a compelling book that has been available on the Amazon platform since the year 2020. This literary work showcases my dedication to crafting engaging content and demonstrates my ability to create meaningful and impactful narratives. The book's presence on Amazon underscores my commitment to sharing my insights and ideas with a wider audience, contributing to both my growth as an author and the enrichment of readers' experiences.
            """
        )
        st.markdown("[See portfolio...](https://www.amazon.com/dp/B08RG7S3KY/ref=tsm_1_fb_lk)")


with st.container():  
    st.write("##")
    image_column, text_column= st.columns((1, 2))
    with image_column:
        st.image(img_coach)
    with text_column:
        st.subheader("Coaching")
        st.write(
            """
               My coaching endeavors are centered around empowering entrepreneurs, drawing from my digital management knowledge to guide them in realizing their visions and achieving their business objectives.My coaching journey has equipped me with valuable insights into effective communication, mentorship, and fostering growth. This experience reflects my dedication to empowering others and nurturing their potential, highlighting my ability to create meaningful and positive impacts in diverse contexts.
            """
        )
        st.markdown("[See portfolio...](https://digitalmanagement.thinkific.com/courses/DigitalManagers)")

# ---- Simple footer ----
with st.container():
    st.write("---")
    st.write("     Thank you for visiting and taking the time to review my online CV.")




if __name__ == "__main__":
    # Run the Streamlit app
    switch_page("home")  # Start with the "home" page




