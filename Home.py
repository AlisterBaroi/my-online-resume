import streamlit as st
from pathlib import Path
import os
import streamlit.components.v1 as components

# https://developer.chrome.com/docs/lighthouse/seo/meta-description/?utm_source=lighthouse&utm_medium=lr
# https://developer.mozilla.org/en-US/docs/Web/Manifest

st.set_page_config(
    page_title="Alister Animesh Baroi - Portfolio Website",
    page_icon=":page_facing_up:",
    layout="centered",
    # initial_sidebar_state="collapsed",
    # menu_items=None
)
st._config.set_option("theme.base", "dark")

# # Include Google Analytics tracking code (doesnt work)
# with open("analytics.html", "r") as f:
#     html_code = f.read()
#     components.html(html_code, height=0)

# components.iframe('analytics.html', height=1, scrolling=False)
# components.html(r'analytics.html')

metadata = """
<h1 style="display: none;">Alister Animesh Baroi | Alister Baroi</h1>
<p style="display: none;">Welcome to the website of Alister Animesh Baroi or Alister Baroi. This is Alisters online portfolio and digital resume website</p>"""
st.markdown(metadata, unsafe_allow_html=True)


# Potential work-around to fixing Google Search Console code integration issue (https://github.com/streamlit/streamlit/issues/6567#issuecomment-2143512104)
# index = Path(st.__file__).parent / "static" / "index.html"
# # os.chmod(index, 0o777)
# html = index.read_text()
# st.write(html)
# metadata = """<meta name='url' content='https://alisterbaroi/streamlit.app'>
# <meta name="author" content="Alister Animesh Baroi, alister.baroi@gmail.com">
# <meta name='copyright' content='Alister Animesh Baroi, alister.baroi@gmail.com'>
# <meta name="application-name" content="Alister Animesh Baroi - Portfolio Website">
# <meta name="google-site-verification" content="OP3yEmLoPHFKz6nzUVU_aWuso0ZWhv2MYBNlE0VQb0k" />
# <meta name="description" content="Welcome to Alister Animesh Baroi's Digital/Online Resume, and portfolio website">
# <meta name="keywords" content="Alister, Alister Baroi, Alister Animesh Baroi, alisterbaroi, AlisterBaroi, AlisterAnimeshBaroi">"""

# # Replace the target string
# if metadata not in html:
#   html = html.replace("<head>", "<head>" + metadata)
#   # Write the file out again
#   with open(index, "w+") as f:
#     f.write(html)
#     print("Inserted metadata into:", index)
# else:
#   print("Metadata not inserted: Already exists")


def main():
    # Dark mode
    with st.sidebar:
        # st.logo("./assets/Alister_Animesh_Baroi.png", link="", icon_image="./assets/profile-pic (1).png")
        if st.toggle("Dark Mode", value=True) is False:
            st._config.set_option(f"theme.base", "light")
        else:
            st._config.set_option(f"theme.base", "dark")

        # Refresh button
        if st.button(
            "Refresh",
            help="Refresh page if something isn't updating accordingly",
            use_container_width=True,
        ):
            st.rerun()

        # Clear button
        if st.button(
            "Clear Session",
            help="Clears session, cache, and cookie data",
            use_container_width=True,
        ):
            st.cache_data.clear()
            st.session_state.clear()
            st.cache_resource.clear()
            st.rerun()
        st.markdown(
            "Copyright ©️ 2024 :blue[Alister Animesh Baroi.]<br>All rights reserved.",
            unsafe_allow_html=True,
        )

    row0 = st.columns([2, 4], gap="medium")

    # Hero Section
    with row0[0]:
        st.image("./assets/Alister-Baroi-Profile-Pic.png", width=230)

    with row0[1]:
        st.header("Alister Animesh Baroi", anchor=False)
        st.write(
            """
             :blue[Cloud Architect, DevOps Engineer, AI Engineer, Backend Engineer]
             *Driving business success with AI-powered workflows & cloud solutions*
              """
        )
        # with open("./assets/Alister_Baroi_Resume.pdf", "rb") as file:
        st.link_button(
            ":page_facing_up: Download Resume",
            url="https://drive.google.com/file/d/1LLs3UgpVucCrWV6vABog660N_gl0Dk43/view",
            type="primary",
        )
        #  data=file, file_name="Alister_Baroi_Resume.pdf", mime="application/pdf"

        # row1 = st.columns([0.8, 1, 1.05, 0.9])
        row1 = st.columns([1, 1, 1])
        row1[0].link_button(
            ":orange[@ Email]",
            url="mailto:alister.baroi@gmail.com",
            help="alister.baroi@gmail.com",
            use_container_width=True,
        )
        # row1[1].link_button(":red[:globe_with_meridians: Website]", url="https://alisterbaroi.streamlit.io", help="alisterbaroi.streamlit.io", use_container_width=True)
        row1[1].link_button(
            ":blue-background[in] :blue[LinkedIn]",
            url="https://www.linkedin.com/in/alisterbaroi",
            help="linkedin.com/in/alisterbaroi",
            use_container_width=True,
        )
        row1[2].link_button(
            ":computer: :green[GitHub]",
            url="https://github.com/alisterbaroi",
            help="github.com/alisterbaroi",
            use_container_width=True,
        )

    st.markdown("<style>hr{margin: 0;}</style>", unsafe_allow_html=True)
    st.divider()

    # Summary Section
    st.subheader("Summary", anchor=False)
    st.markdown(
        """ 
  - About 3+ years of relavant work experience,
  - 👔 Lead Cloud Architect (current job),
  - 🏆 Computer Science (Honours) graduate from Taylors University (Malaysia),
    - 🔥 Majored in AI & minored in FinTech,
  """
    )

    # Skills Section
    st.subheader("Skills", anchor=False)
    with st.expander("Programming Languages"):
        st.multiselect(
            "Programming Languages",
            [
                "Python",
                "JavaScript",
                "Git",
                "YAML",
                "HCL",
                "SQL",
                "PHP",
                "C++",
                "Java",
                "Bash",
                "PowerShell",
                "HTML",
                "CSS",
            ],
            [
                "Python",
                "JavaScript",
                "Git",
                "YAML",
                "HCL",
                "SQL",
                "PHP",
                "C++",
                "Java",
                "Bash",
                "PowerShell",
                "HTML",
                "CSS",
            ],
            disabled=False,
            label_visibility="collapsed",
        )

    with st.expander("Frameworks & Libraries"):
        st.multiselect(
            "Frameworks & Libraries",
            [
                "FastAPI",
                "Streamlit",
                "Docker",
                "Terraform",
                "Django",
                "Seaborn",
                "Keras",
                "Next.js",
                "Anaconda",
                "TensoFlow",
                "Scikit-learn",
                "Matplotlib",
                "React Native",
            ],
            [
                "FastAPI",
                "Streamlit",
                "Docker",
                "Terraform",
                "Django",
                "Seaborn",
                "Keras",
                "Next.js",
                "Anaconda",
                "TensoFlow",
                "Scikit-learn",
                "Matplotlib",
                "React Native",
            ],
            disabled=False,
            label_visibility="collapsed",
        )

    with st.expander("Platforms & Tools"):
        st.multiselect(
            "Platforms & Tools",
            [
                "Google Cloud",
                "GitHub",
                "GitHub Actions",
                "Docker",
                "Linux",
                "Figma",
                "MySQL",
                "PostgreSQL",
                "Google Colab",
                "Jupyter Notebooks",
            ],
            [
                "Google Cloud",
                "GitHub",
                "GitHub Actions",
                "Docker",
                "Linux",
                "Figma",
                "MySQL",
                "PostgreSQL",
                "Google Colab",
                "Jupyter Notebooks",
            ],
            disabled=False,
            label_visibility="collapsed",
        )

    with st.expander("Technology Concepts"):
        st.multiselect(
            "Technology Concepts",
            [
                "Microservices",
                "DevOps",
                "CI/CD",
                "AI",
                "Backend",
                "Data Anaalysis",
                "Data Science",
                "ML",
                "Software Architecture",
                "Prompt Enfineering",
            ],
            [
                "Microservices",
                "DevOps",
                "CI/CD",
                "AI",
                "Backend",
                "Data Anaalysis",
                "Data Science",
                "ML",
                "Software Architecture",
                "Prompt Enfineering",
            ],
            disabled=False,
            label_visibility="collapsed",
        )

    with st.expander("Soft skills"):
        st.multiselect(
            "List of Soft Skills",
            [
                "Python",
                "JavaScript",
                "Git",
                "YAML",
                "SQL",
                "PHP",
                "C++",
                "Java",
                "Bash",
                "PowerShell",
                "HTML",
                "CSS",
            ],
            [
                "Python",
                "JavaScript",
                "Git",
                "YAML",
                "SQL",
                "PHP",
                "C++",
                "Java",
                "Bash",
                "PowerShell",
                "HTML",
                "CSS",
            ],
            disabled=False,
            label_visibility="collapsed",
        )

    # Experience Section
    st.subheader("Relevant Experience", anchor=False)
    with st.expander("Read Global Consultants :gray[(*Oct 2023 - Present*)]"):
        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[Lead Cloud Architect]")
            jobcol[1].write(":grey[London, England, UK (Remote)]")
            jobcol[2].write(":gray[*Mar 2024 - Present*]")
            st.write(
                """
              - Created :green[AI-driven APIs] and systems to streamline the :green[automated workflows] which significantly increased company's internal efficiency,
              - Built different :green[backend microservices] to connect with Google Cloud to perform variety automations for the company's internal and external operations
              - Designed, implimented, and maintained :green[CI/CD pipelines].
               """
            )
        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[Solutions Architect]")
            jobcol[1].write(":grey[London, England, UK (Remote)]")
            jobcol[2].write(":grey[*Oct 2023 - Mar 2024*]")
            st.write(
                """
              - Acquired Google Cloud :green[Startup Funding] as Cloud Credits to enable the company to access Google Cloud for two years at no cost,
              - Did :green[R&D] on designing, implementing, and overseeing the :green[cloud infrastructure] of the company,
              - Designed, implimented, and maintained :green[CI/CD pipelines].
               """
            )

    with st.expander("Kambyan Network :gray[(*Aug 2022 - Jun 2023*)]"):
        with st.container():
            with st.container(border=True):
                jobcol = st.columns([1.5, 1.5, 1])
                jobcol[0].write(":blue[DevOps Engineer]")
                jobcol[1].write(":grey[Petaling Jaya, KL, Malaysia]")
                jobcol[2].write(":grey[*Aug 2022 - Jun 2023*]")
                st.write(
                    """
              - Designed, built and monitored the :green[CI/CD pipelines] which reduced the company's code-to-production interval :green[from 1 hour to 4 minutes],
              - Monitored, analyzed, and optimized the :green[cloud infrastructure] which resulted in a :green[65% reduction of the daily cloud operations cost],
              - Designed :green[microservice architectures], its integration with the cloud, and compliance with the SDLC and Cloud Standards,
              - Designed, implemented, and oversaw the :green[VPC network] and the company's cloud infrastructure.
               """
                )

    with st.expander(
        "Google Developers Student Club at Taylor's University :gray[(*Oct 2021 - Oct 2022*)]"
    ):
        with st.container():
            with st.container(border=True):
                jobcol = st.columns([1.5, 1.5, 1])
                jobcol[0].write(":blue[Technical Associate (Mentor)]")
                jobcol[1].write(":grey[Subang Jaya, Selangor, Malaysia]")
                jobcol[2].write(":grey[*Oct 2021 - Oct 2022*]")
                st.write(
                    """
              - Was responsible for hosting technical events and crash courses on :green[Machine Learning], and :green[Google Cloud Platform], at the university,
              - :green[Conducted webinars and technical events] on cloud computing fundamentals and teaching :green[Google Cloud Platform] to and junior students/newcomers.
               """
                )

    st.markdown(
        "To see the full list of my work experience (from LinkedIn), [click here](https://www.linkedin.com/in/alisterbaroi/details/experience/) ➚",
        unsafe_allow_html=True,
    )

    # Education Section
    st.subheader("Education", anchor=False)
    with st.expander(
        "Bachelor of Computer Science (Hons) :gray[(*Aug 2020 - Aug 2023*)]"
    ):
        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[Bachelor of Computer Science (Hons)]")
            jobcol[1].write(":grey[Taylor' University - Selangor, Malaysia]")
            jobcol[2].write(":grey[*Aug 2020 - Aug 2023*]")
            st.write(
                """
              - Major/specilization in :green[Artificial Intelligence] (AI),
              - Minor in :green[Financial Technology] (FinTech),
              - CGPA: :green[3.54/4.0],
              - Achievements: :green[Deans List] letters of recommendation, :green[Taylor's SHINE Gold Award], :green[Taylor's Excellence Award Scholarship] 
                 """
            )

        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[Bachelor of Science in Computer Science (Hons)]")
            jobcol[1].write(
                ":grey[University of the West of England (UWE) - Bristol, UK]"
            )
            jobcol[2].write(":grey[*Aug 2020 - Aug 2023*]")
            st.write(
                """
              - Dual award program with Taylor's University,  
              - CGPA: :green[3.54/4.0]
               """
            )
    with st.expander("Foundation in Computing :gray[(*Aug 2019 - Aug 2020*)]"):
        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[Foundation in Computing]")
            jobcol[1].write(":grey[Taylor' College - Selangor, Malaysia]")
            jobcol[2].write(":grey[*Aug 2019 - Aug 2020*]")
            st.write(
                """  
              - CGPA: :green[3.44/4.0],
              - Achievements: :green[Deans List] letters of recommendation
               """
            )

    with st.expander("A Levels :gray[(*June 2016 - June 2018*)]"):
        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[Cambridge Advanced Levels]")
            jobcol[1].write(":grey[British Council Bangladesh - Dhaka, Bangladesh]")
            jobcol[2].write(":grey[*June 2016 - June 2018*]")
            st.write(
                """
              - :green[Subjects:] Physics, Chemistry, Mathematics, 
              - :green[Reg. Type:] Private Student 
               """
            )

    with st.expander("O Levels :gray[(*June 2014 - Jun 2015*)]"):
        with st.container(border=True):
            jobcol = st.columns([1.5, 1.5, 1])
            jobcol[0].write(":blue[Cambridge Ordinary Levels]")
            jobcol[1].write(
                ":grey[Bacha English Medium School (BEMS) - Dhaka, Bangladesh]"
            )
            jobcol[2].write(":grey[*June 2014 - Jun 2015*]")
            st.write(
                """
              - :green[Subjects:] English Language, Mathematics, Chemistry, Physics, Bengali, Geography, 
              - :green[Reg. Type:] School Student
               """
            )
    st.markdown(
        "To see more details on my education (from LinkedIn), [click here](https://www.linkedin.com/in/alisterbaroi/details/education/) ➚",
        unsafe_allow_html=True,
    )

    # Projects Section
    st.subheader("Recent Projects", anchor=False)
    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        jobcol[0].write("Resume Parser API")
        jobcol[1].write(
            ":gray[API to accept resume files, process with computer vision & LLM, & send back the parsed data as JSON]"
        )
        jobcol[2].link_button(
            ":red[View Project ➚]",
            url="https://resume-parser-api-2otwbg7hbq-nw.a.run.app/docs",
            use_container_width=True,
        )

    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        jobcol[0].write("Cat & Dog Classifier")
        jobcol[1].write(
            ":gray[A simple app build on top of my custom-made AI model to distinguish between cats & dogs]"
        )
        jobcol[2].link_button(
            ":red[View Project ➚]",
            url="https://cat-and-dog-classifier-5b4x24knra-uc.a.run.app/",
            use_container_width=True,
        )

    st.page_link(
        "pages/1_Projects.py",
        label="To see the list of all my projects in details visit :blue[projects page]",
    )

    # Achievements Section
    st.subheader("Achievements", anchor=False)
    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "award": "Taylor's SHINE Gold Award",
            "type": "Recognition",
            "date": "08/2023",
            "from": "Taylor's University",
            "des": "Taylor's recognition of my outstanding extracurricular activities e.g. hackathons & certifications.",
            "link": "https://drive.google.com/file/d/1Yd-PM_xgaQU6Au_rEhYb10fablGMw5RT/view",
        }
        jobcol[0].write(a["award"])
        jobcol[1].write(
            ":gray[Taylor's recognition of my :green[outstanding extracurricular activities] e.g. hackathons & certifications]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="SHINE"
        ):
            achievements(
                a["award"], a["type"], a["date"], a["from"], a["des"], a["link"]
            )

    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "award": "2nd Prize Winner",
            "type": "Competition",
            "date": "04/2022",
            "from": "Microsoft, FOSSASIA",
            "des": "Placed 2nd out of 2568 contestants, 797 finalists on FOSSASIA Cloud Skills Challenge 2022, a global competition hosted by Microsoft and FOSSASIA.",
            "link": "https://www.linkedin.com/feed/update/urn:li:activity:6918520785208762368/",
        }
        jobcol[0].write(a["award"])
        jobcol[1].write(
            ":gray[Out of 2568 contestants, 797 finalists on :green[FOSSASIA Cloud Skills Challenge 2022], by Microsoft & FOSSASIA]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="FOSSASIA"
        ):
            achievements(
                a["award"], a["type"], a["date"], a["from"], a["des"], a["link"]
            )

    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "award": "4th Place",
            "type": "Competition",
            "date": "06/2021",
            "from": "Taylor's University",
            "des": "Ranked 4th out of 73 contestants at ImagineHack2021 hackathon, a coding competition hosted by Taylor's University.",
            "link": "https://drive.google.com/file/u/1/d/1oA8pHIJU8iYBtqyHCfHs_-Qm7p92JnWp/view",
        }
        jobcol[0].write(a["award"])
        jobcol[1].write(
            ":gray[Ranked 4th out of 73 contestants at :green[ImagineHack2021 hackathon], by Taylor's University]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="ImagineHack2021"
        ):
            achievements(
                a["award"], a["type"], a["date"], a["from"], a["des"], a["link"]
            )

    with st.container(border=True):
        jobcol = st.columns([2, 5, 2])
        a = {
            "award": "Taylor's Excellence Award",
            "type": "Scholarship",
            "date": "08/2020",
            "from": "Taylor's University",
            "des": "Got the Taylor's Excellence Award scholarship for my Bachelor program from exceptional performance during foundations.",
            "link": None,
        }
        jobcol[0].write(a["award"])
        jobcol[1].write(
            ":gray[Got this :green[scholarship] for my Bachelor program from exceptional performance during foundations]"
        )
        if jobcol[2].button(
            ":red[View Details]", use_container_width=True, key="Excellence"
        ):
            achievements(
                a["award"], a["type"], a["date"], a["from"], a["des"], a["link"]
            )

    st.markdown(
        "To see the full list of my achievement (from LinkedIn), [click here](https://www.linkedin.com/in/alisterbaroi/details/honors/) ➚",
        unsafe_allow_html=True,
    )

    # components.iframe("https://github.com/AlisterBaroi/my-resume/blob/e3e8c57ef87e1512eca6e7b22a4100b3d461e0e3/google0be275124e299297.html")


@st.experimental_dialog("Achievement", width="small")
def achievements(item, item2, item3, item4, item5, item6):
    st.write(
        f""":green[Award:]   
                 {item}"""
    )
    details = st.columns([1, 1, 1])
    details[0].write(
        f""":green[Type:]   
                     {item2}"""
    )
    details[1].write(
        f""":green[Date:]   
                     {item3}"""
    )
    details[2].write(
        f""" :green[From:]   
                     {item4}"""
    )
    st.write(
        f""":green[Description:]   
             {item5}"""
    )
    if item6 is None:
        if st.button("Close"):
            st.rerun()
    else:
        btns_finnal = st.columns([2, 1])
        btns_finnal[0].link_button(
            "View Achievement ➚",
            url=item6,
            type="primary",
            use_container_width=True,
        )
        if btns_finnal[1].button("Close", use_container_width=True):

            st.rerun()


# def replace_in_file(filename, oldvalue, newvalue, findvalue):
#     """Replace string in a file and optionally create backup_filename."""
#    # Read in the file
#     with open(filename, "r") as f:
#        filedata = f.read()

#      # Replace the target string
#    if findvalue not in filedata:
#      filedata = filedata.replace(oldvalue, newvalue)
#       Write the file out again
#       with open(filename, "w") as f:
#          f.write(filedata)
#       print("Inserted metadata into:", filename)
#     else:
#       print("Metadata not inserted: Already exists")


if __name__ == "__main__":
    main()
