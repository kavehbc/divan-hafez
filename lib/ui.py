import streamlit as st

from lib.db import get_data, get_connection, search_data
from lib.mp3 import play_audio

URI_SQLITE_DB = "db/hafez.db"


def create_text(text, font="IranNastaliq", font_size=2):
    str_text = f"""
    <div class="custom_text">{text}</div>
    """
    return str_text


def init_ui():
    st.markdown("""
        <link href="https://db.onlinewebfonts.com/c/52ce4de2efeeb8b18dcbd379711224f3?family=B+Yekan" rel="stylesheet" type="text/css"/>
        <link href="https://db.onlinewebfonts.com/c/3b019b0df3b0d6ea4d1b2f051132febb?family=IranNastaliq" rel="stylesheet" type="text/css"/>
        <style>
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
        .custom_text {
      unicode-bidi:bidi-override;
      direction: RTL;
      text-align: right;
      font-family: 'IranNastaliq', Tahoma;
      font-size: 2em;
    }
        </style>
            """, unsafe_allow_html=True)


def show_poem(int_poem, query=None, font_size=1.5):
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

        col1, col2 = st.beta_columns(2)
        verse = 0
        while verse < len(lst_poem):
            with col2:
                if verse < len(lst_poem):
                    st.markdown(create_text(lst_poem[verse], font_size=font_size), unsafe_allow_html=True)
                    verse += 1
            with col1:
                if verse < len(lst_poem):
                    st.markdown(create_text(lst_poem[verse], font_size=font_size), unsafe_allow_html=True)
                    verse += 1

        st.header("تعبیر")
        st.write("")
        st.markdown(create_text(str_interpretation, font_size=font_size), unsafe_allow_html=True)
        st.write("")
        play_audio(int_poem)


def show_search_result(query, font_size):
    conn = get_connection(URI_SQLITE_DB)
    df = search_data(conn, query)
    for index, row in df.iterrows():
        poem_id = row["id"]
        with st.beta_expander(label=f"Poem {poem_id}", expanded=False):
            show_poem(poem_id, query, font_size)
        # st.markdown("___")
