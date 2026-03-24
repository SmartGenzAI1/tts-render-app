FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y espeak-ng

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p output

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
