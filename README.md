# Docker for Machine Learning Pipeline
This repo is an illustration of how a machine learning deployment pipeline can be exposed to different stakeholders (like QA teams) using docker to maintain a uniform and reproducible ML pipeline.<br>
1. A simple machine learning classification pipeline is built using sklearn.
2. The model is exposed to end-users using flask and Swagger.
3. The deployment is dockerized. Several artifacts are generated.
4. The docker image is pushed to dockerhub for public access. The application image can be found [here](https://hub.docker.com/repository/docker/aashish98432/ml_app).
