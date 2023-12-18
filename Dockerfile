# https://hub.docker.com/_/python
FROM python:3.9-slim

ENV PYTHONUNBUFFERED True


ENV APP_HOME /app

WORKDIR $APP_HOME

COPY . ./
RUN apt-get update && apt-get install -y build-essential
RUN pip install -r requirements.txt gunicorn gevent>=1.4
COPY gunicorn.conf.py ./gunicorn.conf.py



# CMD [ "uvicorn", "main:app", "--port", "8000" ]

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

# EXPOSE 8000
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# CMD ["gunicorn", "--config", "/app/gunicorn.conf.py", "--access-logfile", "-", "main:app", "--bind", "0.0.0.0:$PORT"]
