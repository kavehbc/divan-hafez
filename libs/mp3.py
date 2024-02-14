import streamlit as st
import hafez
import os


def get_file_name(id):
    file_name = f"{id:04d}.mp3"
    return file_name


def play_audio(id):

    # mp3_file_path = f'mp3/{get_file_name(id)}'
    mp3_file_path = hafez.get_audio(id)

    if not os.path.exists(mp3_file_path):
        hafez.download_audio(id)

    audio_file = open(mp3_file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio / ogg')
