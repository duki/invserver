#!/bin/bash
sudo docker build -t flask-app .
sudo docker run -p 5000:5000 flask-app

