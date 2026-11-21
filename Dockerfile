FROM python:3.12-slim
WORKDIR /app
COPY UniGap.py .
CMD ["python", "UniGap.py"]


