# setup server
# 1: start docker kernal + python
FROM python:3.9-slim

# Set environment variables
# ENV show lgs
ENV PYTHONUNBUFFERED=1

# 4: create project folder inside the kernal (app)
WORKDIR /app

# 5: copy requirements.txt file to the app folder

COPY requirements.txt ./app/requirements.txt

# 6: install the requirements.txt file

RUN pip install --upgrade pip
RUN pip install -r ./app/requirements.txt

#7: copy project code to docker kernal
COPY . ./app/

