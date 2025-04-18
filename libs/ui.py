import streamlit as st
import hafez
from libs.mp3 import play_audio


def create_text(text, font_name="nastaliq"):
    str_text = f"""
    <div class="custom_{font_name}_text">{text}</div>
    """
    return str_text


def init_ui():
    st.markdown("""
        <style>
        @font-face {
            font-family: "IRANYekan";
            src: url("https://db.onlinewebfonts.com/t/235b71a9b409e684e865eb4a996e925e.eot");
            src: url("https://db.onlinewebfonts.com/t/235b71a9b409e684e865eb4a996e925e.eot?#iefix")format("embedded-opentype"),
            url("https://db.onlinewebfonts.com/t/235b71a9b409e684e865eb4a996e925e.woff2")format("woff2"),
            url("https://db.onlinewebfonts.com/t/235b71a9b409e684e865eb4a996e925e.woff")format("woff"),
            url("https://db.onlinewebfonts.com/t/235b71a9b409e684e865eb4a996e925e.ttf")format("truetype"),
            url("https://db.onlinewebfonts.com/t/235b71a9b409e684e865eb4a996e925e.svg#IRANYekan")format("svg");
        }
        
        @font-face {font-family: "IranNastaliq";
            src: url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.eot"); /* IE9*/
            src: url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.eot?#iefix") format("embedded-opentype"), /* IE6-IE8 */
            url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.woff2") format("woff2"), /* chrome firefox */
            url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.woff") format("woff"), /* chrome firefox */
            url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.ttf") format("truetype"), /* chrome firefox opera Safari, Android, iOS 4.2+*/
            url("https://db.onlinewebfonts.com/t/3b019b0df3b0d6ea4d1b2f051132febb.svg#IranNastaliq") format("svg"); /* iOS 4.1- */
        }
                
        @font-face {
            font-family: "IRAN Sans Regular";
            src: url("https://db.onlinewebfonts.com/t/0b0a8c345731751b990403a2cf40fbec.eot");
            src: url("https://db.onlinewebfonts.com/t/0b0a8c345731751b990403a2cf40fbec.eot?#iefix")format("embedded-opentype"),
            url("https://db.onlinewebfonts.com/t/0b0a8c345731751b990403a2cf40fbec.woff2")format("woff2"),
            url("https://db.onlinewebfonts.com/t/0b0a8c345731751b990403a2cf40fbec.woff")format("woff"),
            url("https://db.onlinewebfonts.com/t/0b0a8c345731751b990403a2cf40fbec.ttf")format("truetype"),
            url("https://db.onlinewebfonts.com/t/0b0a8c345731751b990403a2cf40fbec.svg#IRAN Sans Regular")format("svg");
        }
                
        p, div, input, label {
          /* unicode-bidi:bidi-override;
          direction: RTL;
          text-align: right; */
          font-family: 'IRANYekan', Tahoma;
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
        .custom_iran_sans_text {
          unicode-bidi:bidi-override;
          direction: RTL;
          text-align: right;
          font-family: 'IRAN Sans Regular', Tahoma;
          font-size: 1em;
        }
        </style>
            """, unsafe_allow_html=True)


def highlight(verse, query=None):
    if query is None:
        return verse
    else:
        query = query.strip()
        lst_query = query.split(" ")
        for item in lst_query:
            verse = verse.replace(item, f'<span style="color:red;">{item}</span>')
        return verse


def show_poem(int_poem, query=None, font_name="nastaliq", layout="col2"):

    poem = hafez.get_poem(int_poem)

    st.header(f"غزل شماره {poem['id']}")
    st.write("")

    verse = 0
    while verse < len(poem['poem']):
        with st.container():
            if layout == "col2":
                col1, col2 = st.columns(2)
                with col2:
                    if verse < len(poem['poem']):
                        st.markdown(create_text(highlight(poem['poem'][verse], query), font_name), unsafe_allow_html=True)
                        verse += 1
                with col1:
                    if verse < len(poem['poem']):
                        st.markdown(create_text(highlight(poem['poem'][verse], query), font_name), unsafe_allow_html=True)
                        verse += 1
            elif layout == "col1":
                if verse < len(poem['poem']):
                    st.markdown(create_text(highlight(poem['poem'][verse], query), font_name), unsafe_allow_html=True)
                    verse += 1

    st.header("تعبیر 1")
    st.write("")
    st.markdown(create_text(poem['interpretation'], font_name), unsafe_allow_html=True)
    if len(poem['alt_interpretation']) > 0:
        st.header("تعبیر 2")
        st.write("")
        st.markdown(create_text(poem['alt_interpretation'], font_name), unsafe_allow_html=True)
    st.write("")
    play_audio(int_poem)


def show_search_result(query, font_name, layout="col2"):
    lst_poems = hafez.search(query)

    for poem in lst_poems:
        poem_id = poem["id"]
        with st.expander(label=f"Poem {poem_id}", expanded=False):
            show_poem(poem_id, query, font_name=font_name)
        # st.markdown("___")
