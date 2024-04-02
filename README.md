# Streamlit Web App describing NHL Player Stats 2004 - 2018

This project is done using [Streamlit](https://www.streamlit.io/) framework. The data used in this repo is the [NHL Player Stats](https://www.kaggle.com/datasets/xavya77/nhl04to18/data) from Kaggle. This dataset contains regular and "advanced" statistics for all NHL skaters from the 2004 through the 2018 season.

Try app [here]()!

## Files

- `app.py`: streamlit app file
- `nhl.csv`: data file
- `requirements.txt`: package requirements files

## Run Demo Locally 

### Shell

For directly run streamlit locally in the repo root folder as follows:

```shell
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run app.py
```
Open http://localhost:8501 to view the app.
