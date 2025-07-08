FROM python:3.13-slim
WORKDIR /app
COPY . .
ENV PYTHONPATH="${PYTHONPATH}:/app/src"
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]