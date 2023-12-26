FROM python:3.11
LABEL authors="Sergey"

RUN mkdir fastapi_app
WORKDIR fastapi_app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

#WORKDIR src

#CMD uvicorn src/todolist_api:app --host 0.0.0.0 --port 8000 --reload

#ENTRYPOINT ["top", "-b"]