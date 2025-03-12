FROM python:3.13.2-alpine3.21
LABEL maintainer="Vishnuvardhan" \
      email="vysnu.96@gmail.com" \
      description="This image contains randomly picked tamil movie names. Will try to add features to select movies based on year" \
      version="1.0"
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "hang.py"]
