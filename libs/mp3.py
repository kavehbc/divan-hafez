import streamlit as st
import hafez
import os


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

    # mp3_file_path = f'mp3/{get_file_name(id)}'
    mp3_file_path = hafez.get_audio(id)

    if not os.path.exists(mp3_file_path):
        hafez.download_audio(id)

    audio_file = open(mp3_file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio / ogg')
