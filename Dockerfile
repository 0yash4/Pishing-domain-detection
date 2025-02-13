FROM python:3.11

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Set a default port if $PORT is not provided
ENV PORT 8501

EXPOSE $PORT

CMD streamlit run app.py --server.port $PORT --server.address 0.0.0.0

