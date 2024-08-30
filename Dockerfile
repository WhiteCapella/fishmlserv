#FROM python:3.11
FROM python:3.11.9-slim-bullseye
#FROM python:3.11.9-alpine

# 
WORKDIR /code

# 
COPY . /code/

# 
RUN pip install -r /code/requirements.txt

# 
CMD ["uvicorn", "src.fishmlserv.main:app", "--host", "0.0.0.0", "--port", "8000"]
