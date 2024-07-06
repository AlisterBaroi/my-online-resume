import streamlit as st

st.set_page_config(
    page_title="Alister Baroi", page_icon=":page_facing_up:", layout="centered"
)


def main():
    st.title("About —")
    st.write(
        "This website is build by me :red[(Alister Baroi / Alister Animesh Baroi)], as my online resume, & as my porfolio website, to showcase coding skills & projects."
    )
    st.write(
        "This website is made with web app behavior and user interactivity in mind, thus focusing on the :green[User Interface] & :green[User Experience (UI/UX)] for elivated engagement."
    )

    st.divider()
    streamlit_row = st.columns([3, 2])
    with streamlit_row[0]:
        st.subheader(":red[Made with Streamlit]")
        st.write(
            "This web application is build using :red[Streamlit], a free and open-source python web framework, build for rapidly developing & deploying data-driven web apps."
        )
        st.page_link("https://streamlit.io", label=":red[Visit Streamlit.io]")
    streamlit_row[1].image("./assets/streamlit.jpg")

    # Dark mode
    with st.sidebar:
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


if __name__ == "__main__":
    main()
