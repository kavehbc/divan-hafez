import streamlit as st


def get_file_name(id):
    if id < 10:
        str_i = "000" + str(id)
    elif 10 <= id < 100:
        str_i = "00" + str(id)
    elif 100 <= id < 1000:
        str_i = "0" + str(id)

    file_name = str_i + ".mp3"
    return file_name


def play_audio(id):
    audio_file = open(f'mp3/{get_file_name(id)}', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio / ogg')
