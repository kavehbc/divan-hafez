import streamlit as st

from libs.db import get_data, get_connection, search_data
from libs.mp3 import play_audio

URI_SQLITE_DB = "db/hafez.db"


def create_text(text, font_name="nastaliq"):
    str_text = f"""
    <div class="custom_{font_name}_text">{text}</div>
    """
    return str_text


def init_ui():
    st.markdown("""
        <style>
        @font-face {font-family: "B Yekan";
            src: url("https://db.onlinewebfonts.com/t/52ce4de2efeeb8b18dcbd379711224f3.eot"); /* IE9*/
            src: url("https://db.onlinewebfonts.com/t/52ce4de2efeeb8b18dcbd379711224f3.eot?#iefix") format("embedded-opentype"), /* IE6-IE8 */
            url("https://db.onlinewebfonts.com/t/52ce4de2efeeb8b18dcbd379711224f3.woff2") format("woff2"), /* chrome firefox */
            url("https://db.onlinewebfonts.com/t/52ce4de2efeeb8b18dcbd379711224f3.woff") format("woff"), /* chrome firefox */
            url("https://db.onlinewebfonts.com/t/52ce4de2efeeb8b18dcbd379711224f3.ttf") format("truetype"), /* chrome firefox opera Safari, Android, iOS 4.2+*/
            url("https://db.onlinewebfonts.com/t/52ce4de2efeeb8b18dcbd379711224f3.svg#B Yekan") format("svg"); /* iOS 4.1- */
        }
        
        @font-face {font-family: "IranNastaliq";
            src: url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.eot"); /* IE9*/
            src: url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.eot?#iefix") format("embedded-opentype"), /* IE6-IE8 */
            url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.woff2") format("woff2"), /* chrome firefox */
            url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.woff") format("woff"), /* chrome firefox */
            url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.ttf") format("truetype"), /* chrome firefox opera Safari, Android, iOS 4.2+*/
            url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.svg#IranNastaliq") format("svg"); /* iOS 4.1- */
        }
        p, div, input, label {
          /* unicode-bidi:bidi-override;
          direction: RTL;
          text-align: right; */
          font-family: 'B Yekan', Tahoma;
        }
        .found-query {
            font-weight: bold;
            color: red;
        }
        .custom_nastaliq_text {
          unicode-bidi:bidi-override;
          direction: RTL;
          text-align: right;
          font-family: 'IranNastaliq', Tahoma;
          font-size: 2em;
        }
        .custom_yekan_text {
          unicode-bidi:bidi-override;
          direction: RTL;
          text-align: right;
          font-family: 'B Yekan', Tahoma;
          font-size: 1em;
        }
        </style>
            """, unsafe_allow_html=True)


def show_poem(int_poem, query=None, font_name="nastaliq", layout="col2"):
    conn = get_connection(URI_SQLITE_DB)
    df = get_data(conn, int_poem)

    if df.shape[0] > 0:
        st.header(f"غزل شماره {int_poem}")
        st.write("")

        for index, row in df.iterrows():
            str_poem = row["Poem"]
            str_interpretation = row["Interpretation"]

            if query is not None:
                if len(query) > 0:
                    lst_query = query.split(" ")
                    for item in lst_query:
                        str_poem = str_poem.replace(item, f"<span class='found-query'>{item}</span>")
        lst_poem = str_poem.split("\\r\\n")

        verse = 0
        while verse < len(lst_poem):
            with st.container():
                if layout == "col2":
                    col1, col2 = st.columns(2)
                    with col2:
                        if verse < len(lst_poem):
                            st.markdown(create_text(lst_poem[verse], font_name), unsafe_allow_html=True)
                            verse += 1
                    with col1:
                        if verse < len(lst_poem):
                            st.markdown(create_text(lst_poem[verse], font_name), unsafe_allow_html=True)
                            verse += 1
                elif layout == "col1":
                    if verse < len(lst_poem):
                        st.markdown(create_text(lst_poem[verse], font_name), unsafe_allow_html=True)
                        verse += 1

        st.header("تعبیر")
        st.write("")
        st.markdown(create_text(str_interpretation, font_name), unsafe_allow_html=True)
        st.write("")
        play_audio(int_poem)


def show_search_result(query, font_name, layout="col2"):
    conn = get_connection(URI_SQLITE_DB)
    df = search_data(conn, query)
    for index, row in df.iterrows():
        poem_id = row["id"]
        with st.expander(label=f"Poem {poem_id}", expanded=False):
            show_poem(poem_id, query, font_name=font_name)
        # st.markdown("___")
