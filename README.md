# flask-docker-app
Rest Api with Python Flask and deploy to docker


docker build --tag flaskdockerapp:latest .

docker run -p 5000:5000 -t -i flaskdockerapp:latest

or 

docker run -d -p 80:5000 flaskdockerapp

