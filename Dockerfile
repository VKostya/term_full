FROM python:3.9

WORKDIR /app

RUN apt-get update 

RUN apt-get install sqlite3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]