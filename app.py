import streamlit as st
import random

from lib.ui import create_text, init_ui, show_poem, show_search_result


def main():
    st.title("دیوان حافظ")
    st.markdown("___")

    int_poem = st.sidebar.number_input("َPoem #", min_value=1, max_value=495, step=1)
    btn_show_poem = st.sidebar.button("نمایش غزل")
    str_query = st.sidebar.text_input("َSearch Query")
    btn_search_poem = st.sidebar.button("جستجو")
    btn_fall = st.button("فال حافظ")

    if btn_fall:
        int_poem = random.randint(1, 495)

    if btn_search_poem:
        if len(str_query) == 0:
            st.error("جهت جستجو عبارت مورد نظر را وارد نمایید.")
        else:
            show_search_result(str_query)

    elif btn_show_poem or btn_fall:
        show_poem(int_poem)

    else:
        with open('db/home.md', 'r', encoding="utf-8") as outfile:
            md_text = outfile.read()

        lst_md_text = md_text.split("\n")
        for paragraph in lst_md_text:
            st.markdown(create_text(paragraph, font="B Yekan", font_size="1em"), unsafe_allow_html=True)


if __name__ == '__main__':
    st.set_page_config("Divan-e Hafez")
    init_ui()
    main()
