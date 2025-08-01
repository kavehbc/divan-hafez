import streamlit as st
import random
import hafez
from user_agents import parse
from libs.constants import *
from libs.injection import manage_injections
from libs.readme import show_readme
from libs.ui import create_text, init_ui, show_poem, show_search_result

def is_mobile():
    """Check if the user is on a mobile device."""
    user_agent = st.context.headers.get('User-Agent')
    if user_agent:
       ua = parse(user_agent)
       if ua.is_mobile:
           return True
       else:
           return False
    else:
       return False

def pg_about():
    show_readme()
    st.stop()

def pg_download():
    st.title("دانلود صدا")
    st.markdown("___")
    btn_download = st.button("بارگیری دکلمه تمام اشعار")
    if btn_download:
        st_download_progress = st.progress(0, text="Downloading...")
        for item in hafez.download_all_audio():
            st_download_progress.progress(item / 495, text=f"Downloading {item}...")

        st_download_progress.progress(100, text=f"Download Completed.")

def pg_app():
    st.title("دیوان حافظ")
    st.markdown("___")

    with st.sidebar.expander("غزلیات", expanded=True):
        int_poem = st.number_input("َشماره غزل", min_value=1, max_value=495, step=1)
        btn_show_poem = st.button("نمایش غزل")

    with st.sidebar.expander("جستجو", expanded=True):
        str_query = st.text_input("َعبارت جستجو")
        # to check if the search query should be word by word or not
        chk_exact = st.checkbox("جستجوی دقیق", value=True)
        btn_search_poem = st.button("جستجو")

    with st.sidebar.expander("تنظیمات", expanded=True):
        font_name = st.selectbox("نام قلم", options=list(FONT_NAMES.keys()), index=0,
                                        format_func=lambda x: FONT_NAMES[x])

        st_poem_layout = st.selectbox("چیدمان شعر", options=list(POEM_LAYOUT_OPTIONS.keys()),
                                            index=0 if is_mobile() else 1,
                                            format_func=lambda x: POEM_LAYOUT_OPTIONS[x])

    font_size = 2
    # font_size = st.sidebar.number_input("Font Size", min_value=0.5, max_value=5.0, value=1.5, step=0.1)

    btn_fall = st.button("نمایش فال حافظ")

    if btn_fall:
        int_poem = random.randint(1, 495)

    if btn_search_poem:
        if len(str_query) == 0:
            st.error("جهت جستجو عبارت مورد نظر را وارد نمایید.")
        else:
            show_search_result(str_query, exact_match=chk_exact, font_name=font_name, layout=st_poem_layout)

    elif btn_show_poem or btn_fall:
        show_poem(int_poem, font_name=font_name, layout=st_poem_layout)

    else:
        with open('db/home.md', 'r', encoding="utf-8") as outfile:
            md_text = outfile.read()

        lst_md_text = md_text.split("\n")
        for paragraph in lst_md_text:
            st.markdown(create_text(paragraph, font_name="yekan"), unsafe_allow_html=True)
            
def main():

    pages = [
            st.Page(pg_app, title="دیوان حافظ", icon="📖", default=True),
            st.Page(pg_download, title="دانلود صدا", icon="📲"),
            st.Page(pg_about, title="درباره برنامه", icon="📌")
        ]

    pg = st.navigation(pages)
    pg.run()


if __name__ == '__main__':
    st.set_page_config(
    page_title="Divan-e Hafez",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'https://github.com/kavehbc/divan-hafez',
        'Report a bug': "https://github.com/kavehbc/divan-hafez",
        'About': "# UI for `hafez` PyPi package."
        }
    )
    
    # inject required HTML/CSS/JS into the project
    manage_injections()
    init_ui()
    main()
