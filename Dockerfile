FROM python:3.7

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .

# Install Python packages
RUN pip install --upgrade pip \
    pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

EXPOSE 5000

ENV FLASK_APP=application.py

CMD ["flask", "run", "--host", "0.0.0.0"]