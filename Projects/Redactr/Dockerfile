From python:3.11-alpine

WORKDIR /app

# Set Python Path to include /app
ENV PYTHONPATH=/app

ADD . /app

ADD ./scripts /app

COPY ./static/index.css /app/index.css

COPY ./templates/index.html /app/index.html

RUN python3 -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]

CMD sh -c "uvicorn scripts.backend:app --host 0.0.0.0 --port $PORT"
