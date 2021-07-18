# base image of the docker file on top of which the other libraries and the application work
FROM python:3.6-stretch

# creater info
LABEL maintainer="AASHISH ADHIKARI, aashish98432@gmail.com"\
      description="Docker for ML Project Demo"

# copy the files of the project into the root directory of the docker image
COPY app.py /Docker_for_ML/app.py
COPY requirements.txt /Docker_for_ML/requirements.txt
COPY svm_classifier.py /Docker_for_ML/svm_classifier.py
COPY svm_model.pkl /Docker_for_ML/svm_model.pkl

# since we use port 8888 in the app, we expose only this port in this image. the local machine that runs the docker
# container from this image will be able to connect to only this port of the container.
EXPOSE 8888

# define the root directory for the container that will be created; helpful in running the RUN command below
WORKDIR /Docker_for_ML

# verify that the python and pip version required are available [OPTIONAL]
RUN python3 --version
RUN pip3 --version

# install all the dependencies in the container once the container is created.
# VVI : DO NOT USE pip3 freeze > requirements.txt to generate the dependency list. Will include unnecessary dependencies
# and break the docker image build process. Here, used PyCharm's library sync feature to generate the text.
RUN pip3 install -r requirements.txt

# run the application that was built for this image.
CMD python3 app.py