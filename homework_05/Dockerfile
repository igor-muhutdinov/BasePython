FROM python:3.9.6-buster

WORKDIR /web-app

RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml .
RUN poetry install

COPY ./web-app .

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

EXPOSE 80

CMD ["flask", "run", "--host=0.0.0.0"]

# для запуска ввести строку:
# sudo docker run -p 80:80 web-app