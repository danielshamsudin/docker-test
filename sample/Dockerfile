FROM python:3.14.3-alpine
WORKDIR /python-app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY main.py main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]