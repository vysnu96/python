FROM python:3.13.2-alpine3.21
LABEL maintainer="Vishnuvardhan" \
      email="vysnu.96@gmail.com" \
      description="Flag quiz. Play a quiz guessing the country name by their flags. This one is without storing any result data.Check my another repo for with mongo DB." \
      version="1.0"
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "flag.py"]
