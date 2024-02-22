# docker build --progress=plain --no-cache -t kavehbc/divan-hafez .
# docker save -o divan-hafez.tar kavehbc/divan-hafez
# docker load --input divan-hafez.tar

FROM python:3.9-buster

LABEL version="1.0.2"
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