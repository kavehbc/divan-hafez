import streamlit as st
import random

from libs.constants import *
from libs.injection import manage_injections
from libs.readme import show_readme
from libs.ui import create_text, init_ui, show_poem, show_search_result
import hafez


def main():
    st_app_menu = st.sidebar.selectbox("Main Menu", options=list(MENU_OPTIONS.keys()), index=0,
                                       format_func=lambda x: MENU_OPTIONS[x])
    if st_app_menu == "about":
        show_readme()
        st.stop()

    elif st_app_menu == "app":

        st.title("دیوان حافظ")
        st.markdown("___")

        int_poem = st.sidebar.number_input("َPoem #", min_value=1, max_value=495, step=1)
        btn_show_poem = st.sidebar.button("نمایش غزل")
        str_query = st.sidebar.text_input("َSearch Query")
        btn_search_poem = st.sidebar.button("جستجو")

        font_name = st.sidebar.selectbox("Font Name", options=list(FONT_NAMES.keys()), index=0,
                                         format_func=lambda x: FONT_NAMES[x])
        st_poem_layout = st.sidebar.selectbox("Poem Layout", options=list(POEM_LAYOUT_OPTIONS.keys()), index=1,
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
                show_search_result(str_query, font_name=font_name, layout=st_poem_layout)

        elif btn_show_poem or btn_fall:
            show_poem(int_poem, font_name=font_name, layout=st_poem_layout)

        else:
            with open('db/home.md', 'r', encoding="utf-8") as outfile:
                md_text = outfile.read()

            lst_md_text = md_text.split("\n")
            for paragraph in lst_md_text:
                st.markdown(create_text(paragraph, font_name="yekan"), unsafe_allow_html=True)


if __name__ == '__main__':
    st.set_page_config("Divan-e Hafez")

    # inject required HTML/CSS/JS into the project
    manage_injections()
    init_ui()
    main()
