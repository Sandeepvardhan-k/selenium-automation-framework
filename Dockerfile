FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver

COPY . .

CMD ["pytest", "tests/test_login.py", "-v", "--html=reports/report.html"]