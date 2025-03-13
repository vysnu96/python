FROM python:3.13.2-alpine3.21
LABEL maintainer="Vishnuvardhan" \
      email="vysnu.96@gmail.com" \
      description="Flag quiz. Play a quiz guessing the country name by their flags." \
      version="1.0"
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV APP_PORT=0.0.0.0
ENV MONGO_URL
ENV SECRET_KEY
EXPOSE 5000
ENTRYPOINT ["python", "flags.py"]