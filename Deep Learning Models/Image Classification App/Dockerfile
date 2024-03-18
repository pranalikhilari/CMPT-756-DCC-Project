FROM python:3.7

WORKDIR /frontend

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /frontend

CMD [ "streamlit","run","frontend.py" ]