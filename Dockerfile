#FROM python:3.11
FROM whitecapella/fishmlserv:0.5.1
#FROM python:3.11.9-alpine

# 
WORKDIR /code

# 
#COPY . /code/
COPY src/fishmlserv/main.py /code/
COPY src/fishmlserv/model.pkl /code/
#COPY requirements.txt /code/

# 
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install git+https://github.com/WhiteCapella/fishmlserv.git@0.6/webpage

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
