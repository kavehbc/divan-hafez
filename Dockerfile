# docker build --progress=plain --no-cache -t kavehbc/divan-hafez:latest -t kavehbc/divan-hafez:1.0.11 .
# docker save -o divan-hafez.tar kavehbc/divan-hafez
# docker load --input divan-hafez.tar

FROM python:3.11-slim

LABEL version="1.0.11"
LABEL maintainer="Kaveh Bakhtiyari"
LABEL url="http://bakhtiyari.com"
LABEL vcs-url="https://github.com/kavehbc/divan-hafez"
LABEL description="Divan-e Hafez with Interpretations and Vocal Audios"

WORKDIR /app
COPY requirements.txt requirements.txt

# installing the requirements
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]