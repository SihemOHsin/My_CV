from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir.parent / "styles" / "main.css"
resume_file = current_dir.parent / "assets" / "CV.pdf"
profile_pic = current_dir.parent / "assets" / "sihem.png"
favicon = "https://res.cloudinary.com/dvz16ceua/image/upload/v1692056331/sihem/favicon_q0aqzk.ico"


# --- GENERAL SETTINGS ---
NAME = "Sihem Ouled Hsin"
DESCRIPTION = """
Junior developer, interested in python.
"""
EMAIL = "sihemouledhsin@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sihem-ouled-hsin",
    "GitHub": "https://github.com/SihemOHsin",
    "Leetcode": "https://leetcode.com/SihemOuledHsin",
}
PROJECTS = {
    "🏅 Stock management system Dashboard - web application with JEE ,mySql & Xamp": "https://github.com/SihemOHsin/JEE_stockProject",
    "🏅 Stock microservice for ERP - PFA project with springBoot, Eureka, keycloak & sqlserver": "https://www.asm-tunisie.com/logiciel-erp-dux",
    "🏅 Orders microservices - end of the year shool project with asp.net ,gateway Ocelot,RabbitMQ ": "https://github.com/SihemOHsin/.net_microservicesProject",
    "🏅 Angular project- Adding 8 charts to a dashboard with hightcharts ,back php ,mysql, laragon": "https://youtu.be/jBgfGmO02LM",
    "🏅 Desktop Application - Gui app with tkinter & sqlite": "https://github.com/SihemOHsin/GoalsForBetterDays",
    "🏅 Ecommerce App - end of the year school project with nodeJs, MongoDB Atlas Database & angular": "https://github.com/SihemOHsin/NodeJs-EcommerceBackend",
    "🏅 Vitrine website - my own website VirtuA Agency with wordpress": "https://virtuaagency.tn/",
    "🏅 Blog - Annex Blog Website for VirtuA Agency with WordPress": "https://shop.virtuaagency.tn/blog/",
    "🏅 Catalog website - Ste SOH ALU for aluminuim officiel website with wordpress": "https://sohaluminium.tn",
    "🏅 Vitrine Website - Ste Affes Freres Official Juice Company Website with WordPress": "https://affesfreres.com",
    "🏅 Booking website - Dar Lella Aicha guest house website with wordpress": "https://affesfreres.com"



}

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.header(NAME)
    st.write(DESCRIPTION)
    st.write("📞 +216 20 817 717")
    st.write("📫", EMAIL)
    
    # --- SOCIAL LINKS ---
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
        
    st.write('\n')
    st.download_button(
    label=" 📄 Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream")

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
        




# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.write('\n')

st.write(
    """
      Seamlessly moved from a medical background to the IT realm through self-study and determination, showcasing a natural affinity for coding. Driven by a love for technology and a determination to create meaningful digital experiences.

"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Technical Proficiencies")
st.write("---")
st.write(
    """
- ► Programming: Python ,Java, SQL ,HTML/CSS
- ► Framework: Angular, Springboot
- ► Devops: Git , Jenkins, Docker
- ► Databases: SQL server, MongoDB, MySQL ,SQLite
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experience")
st.write("---")

# --- JOB 1
st.write("‍💻", "**Internship | asm - All Soft Multimedia**")
st.write("04/2023 - 07/2023")
st.write(
    """
- ► Contribute to the development of a Stock microservice for an ERP system.
- ► Development tools: java 8, sql server, mongo db ,Keyckloak, Gradle, Git, Docker
- ► Framework: Springboot,Angular
"""
)

# --- JOB 2
st.write('\n')
st.write("‍💻", "**Ebusiness Consultant | VirtuA Agency**")
st.write("10/2020 - 12/2022")
st.write(
    """
- ► Managing legal and financial matters as the creator of the company.
- ► Providing coaching and creating online ad campaigns for clients.
- ► Responsible of online brand positioning for clients and launching new products.
"""
)

# --- JOB 3
st.write('\n')
st.write("‍💻", "**Executive Assistant | Medlife**")
st.write("04/2016 - 10/2020")
st.write(
    """
- ► Contacting medical suppliers and negotiating the products qualifications, legal papers and prices.
- ► Preparing tenders.
- ► Preparing invoices and support the staff to ensure a high-performance customer service.
"""
)

# --- JOB 4
st.write('\n')
st.write("‍💻", "**Public Relations Assistant | AMUT - Association des Médecins Unis pour la Tunisie**")
st.write("01/2015 - 09/2015")
st.write(
    """
- ► Preparing reports on the association's activities.
- ► The organization Of the Faculty of Medicine's awareness event.
- ► Execution of the Third Medical Conference of the association.
"""
)

# --- JOB 5
st.write('\n')
st.write("‍💻", "**Showroom Sales Specialist | Nameco healthcare**")
st.write("01/2015 - 09/2015")
st.write(
    """
- ► Selling medical equipments and hospitals furniture.
- ► Preparing monthly reports about the showroom sales targets.
- ► Dealing with company visitors , clients and employees.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

