FROM python:3.12-slim

# Copy local code to the container image:
WORKDIR /rest_api
COPY . ./

# Install production dependencies:
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8080", "--timeout", "60"]
