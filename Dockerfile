
FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED=1 


RUN apt-get update && apt-get -y install gcc libpq-dev

# 4: Create project folder in kernal
WORKDIR /app

# 5: copy requirements
COPY requirements.txt /app/requirements.txt

# 6: install requirements 
RUN pip install -r /app/requirements.txt

# 7: Copy project code in  doker
COPY . /app/