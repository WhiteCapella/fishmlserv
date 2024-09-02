#FROM python:3.11
FROM python:3.11.9-slim-bullseye
#FROM python:3.11.9-alpine

# 
WORKDIR /code

# 
#COPY . /code/
COPY src/fishmlserv/main.py /code/

# 
RUN pip install -r /code/requirements.txt
#RUN pip install git+https://<MY_PIP_GITHUB_URL>

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
