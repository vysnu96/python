# :triangular_flag_on_post: Flag quiz
This app is a simple quiz by guessing the name of a country with it's flag. You can select the continent and all the flags of it's countries are shown one by one.
You can run this code in your local machine. 

I have dockerized the app and available at docker hub 
```sh
https://hub.docker.com/r/vysnu96/flag-quiz-without-db
```
Or else, use the below command to run the docker image
```sh
docker run --rm -d -p 5000:5000 --name=flag_quiz vysnu96/flag-quiz-without-db:80
```
