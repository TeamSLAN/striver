FROM python:3

ENV PIP_ROOT_USER_ACTION=ignore
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app
COPY . .

RUN pip install gunicorn

CMD [ "gunicorn", \
    "--workers", "1", \
    "--bind", "0.0.0.0:8013", \
    "striver:app" ]
