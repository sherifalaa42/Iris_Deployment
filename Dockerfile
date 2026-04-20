FROM python:3.10-slim

WORKDIR /Iris_Deployment

COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.txt

COPY . /Iris_Deployment

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]