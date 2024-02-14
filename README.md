# Divan-e Hafez

This is a UI for Diven-e Hafez with Fall-e Hafez (`hafez` python package) using Streamlit.
The poems come with interpretations and vocal audios.

## Hafez Python Package
For more information about the Database and Vocal audios, please check `hafez` library:

- https://github.com/kavehbc/hafez
- https://pypi.org/project/hafez/

This package can be installed using `pip`:

```bash
pip install hafez
```

## Demo
You can access the demo version deployed on Streamlit server at:

[https://divan-hafez.streamlitapp.com/](https://divan-hafez.streamlitapp.com/)

## Run
In order to run this tool, you must have Streamlit installed on your machine/environment:

    streamlit run app.py

## Run on Docker
This application is available on [Docker Hub](https://hub.docker.com/r/kavehbc/divan-hafez), and it can be run directly using:

    docker run -p 80:8501 kavehbc/divan-hafez

Once you run it, you can open it in your browser on [http://127.0.0.1](http://127.0.0.1).

> **Apple M1 Silicon - Arm64**
> 
> As of today (`30 May 2021`), this Docker Image is not compatible with `Apple M1 Silicon`.
> Instead, the source code can be run using `conda` on `Rosetta 2`.

## Github Repo
This project is open-source, and it is available on Github at [https://github.com/kavehbc/divan-hafez](https://github.com/kavehbc/divan-hafez).

## Usage Tracking
### User Hits/Views
The app usage is tracked using [statcounter.com](https://statcounter.com/),
and it does not contain any personal information. The file containing the script is located at
`injection\statcounter.html`.

Injection functions are managed inside `libs\injection.py`.

## Developer(s)
Kaveh Bakhtiyari - [Website](http://bakhtiyari.com) | [Medium](https://medium.com/@bakhtiyari)
  | [LinkedIn](https://www.linkedin.com/in/bakhtiyari) | [GitHub](https://github.com/kavehbc)

## Contribution
Feel free to join the open-source community and contribute to this repository.
