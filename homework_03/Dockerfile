FROM python:3.9.6-buster

WORKDIR /web-app

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

COPY ./web-app .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]

# для запуска ввести строку:
# sudo docker run -p 8000:8000 web-app