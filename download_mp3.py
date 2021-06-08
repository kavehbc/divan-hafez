import streamlit as st
import requests


def main():
    st.title("Download MP3")
    status = st.empty()
    for i in range(1, 496):
        if i < 10:
            str_i = "000" + str(i)
        elif i >= 10 and i < 100:
            str_i = "00" + str(i)
        elif i >= 100 and i < 1000:
            str_i = "0" + str(i)

        href = f"https://de.loveziba.com/2019/10/{str_i}.mp3"
        with requests.Session() as req:
            name = "mp3/" + str_i + ".mp3"
            status.info(f"Downloading {name}")
            download = req.get(href)
            if download.status_code == 200:
                with open(name, 'wb') as f:
                    status.info(f"Saving {name}")
                    f.write(download.content)
            else:
                status.error(f"Download Failed For File {name}")


if __name__ == '__main__':
    main()
