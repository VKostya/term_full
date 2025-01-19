FROM python:3.9

WORKDIR /app

RUN apt-get update 

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Jinja2 --upgrade
RUN pip install alembic --upgrade

COPY ./app .

RUN alembic upgrade head

CMD ["python", "main.py"]