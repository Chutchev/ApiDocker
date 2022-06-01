FROM python:3.9-alpine
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]