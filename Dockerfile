#FROM python:3.11
FROM datamario24/python311scikitlearn-fastapi:1.0.0
#FROM python:3.11.9-alpine

# 
WORKDIR /code

# 
#COPY . /code/
COPY src/fishmlserv/main.py /code/
#COPY requirements.txt /code/

# 
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install git+https://github.com/WhiteCapella/fishmlserv.git@0.5

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "0001"]
