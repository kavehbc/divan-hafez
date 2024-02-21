import streamlit as st
import hafez
import os
import requests


def get_file_name(id):
    file_name = f"{id:04d}.mp3"
    return file_name


def play_audio(id):

    # mp3_file_path = f'mp3/{get_file_name(id)}'
    mp3_file_path = hafez.get_audio(poem=id, download=False)

    if str(mp3_file_path).startswith("http"):
        with requests.Session() as req:
            download = req.get(mp3_file_path)
            if download.status_code == 200:
                audio_bytes = download.content
            else:
                st.error("There was an issue to download the sound.")
    else:
        audio_file = open(mp3_file_path, 'rb')
        audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio / ogg')
