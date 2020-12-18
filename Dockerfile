From python:3.6.12-alpine

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]