# :triangular_flag_on_post: Flag quiz
I developed this python application using Flask. It uses mongo for database. In this application, you will be asked to select a continent and find the country name for the displayed flag image.

Application is available at port 5000 and mongo express UI is available at 8081.

### Docker compose deployment
To deploy it in docker compose, use the command
```sh
docker compose -f docker-compose.yaml up -d
```
If docker compose is installed as standalone as opposed to a plugin as mentioned above, use the command
```sh
docker-compose -f docker-compose.yaml up -d
```

### Kubernetes Deployment
Use the command to install it in k8s cluster. 
Application is available at port 32001 and mongo express UI is available at 32011.
```sh
kubectl apply -f k8s-deployment.yaml
```
