From python:3.11-alpine

WORKDIR /app

# Set Python Path to include /app
ENV PYTHONPATH=/app

ADD . /app

ADD ./scripts /app


RUN python3 -m pip install --no-cache-dir -r requirements.txt


EXPOSE 8000

# CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8000"]

CMD sh -c "uvicorn backend:app --host 0.0.0.0 --port $PORT"
