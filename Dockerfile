# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim-buster

ARG DB_HOST
ENV DB_HOST=${DB_HOST}

ARG DB_PORT
ENV DB_PORT=${DB_PORT}

ARG DB_NAME
ENV DB_NAME=${DB_NAME}

ARG DB_USER
ENV DB_USER=${DB_USER}

ARG DB_PASS
ENV DB_PASS=${DB_PASS}

ARG DEBUG
ENV DEBUG=${DEBUG}

ARG SECRET_KEY
ENV SECRET_KEY=${SECRET_KEY}}

ENV APP_HOME /app
WORKDIR $APP_HOME

# Install dependencies.
COPY requirements.txt .
RUN pip install -U pip && pip install -r requirements.txt

# Copy local code to the container image.
COPY . .

# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8000

# Setting this ensures print statements and log messages
# promptly appear in Cloud Logging.
ENV PYTHONUNBUFFERED TRUE

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 config.wsgi:application