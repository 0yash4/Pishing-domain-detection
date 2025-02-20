FROM python:3.11

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Set a default port if $PORT is not provided
ENV PORT 8000

EXPOSE $PORT

CMD uvicorn main:app --host 0.0.0.0 --port 8000 --reload

