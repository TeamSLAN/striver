FROM python:3

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system --deploy

WORKDIR /usr/src/app
COPY . .

RUN pip install gunicorn

# t2.micro has 1 physical core -> 3 workers
CMD [ "gunicorn", \
    "--workers", "3", \
    "--bind", "0.0.0.0:5000", \
    "striver:app" ]
