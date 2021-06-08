# docker build --progress=plain --no-cache -t divan-hafez .
# docker save -o divan-hafez.tar divan-hafez
# docker load --input divan-hafez.tar

FROM python:3.8-buster

LABEL version="1.0.0"
LABEL maintainer="Kaveh Bakhtiyari"
LABEL url="http://bakhtiyari.com"
LABEL vcs-url="https://github.com/kavehbc/divan-hafez"
LABEL description="Divan-e Hafez with Interpretations and Vocal Audios"

WORKDIR /app
COPY . .

# installing the requirements
RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]