FROM python:3.11.6-slim-bullseye

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .

# Install Python packages
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=run.py

CMD ["flask", "run", "--host", "0.0.0.0"]