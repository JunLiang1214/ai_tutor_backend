FROM python:3.9-buster

WORKDIR /app

COPY . /app
RUN apt-get update && apt-get install -y build-essential
RUN pip install -r requirements.txt gunicorn gevent>=1.4
COPY gunicorn.conf.py /app/gunicorn.conf.py



EXPOSE 8080
# CMD [ "uvicorn", "main:app", "--port", "8000" ]
CMD ["gunicorn", "--config", "/app/gunicorn.conf.py", "--access-logfile", "-", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# EXPOSE 8080
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

# CMD ["gunicorn", "--config", "/app/gunicorn.conf.py", "--access-logfile", "-", "main:app", "--bind", "0.0.0.0:$PORT"]
