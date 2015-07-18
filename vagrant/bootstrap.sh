#!/bin/bash

apt-get update
apt-get install vim -y
apt-get install python-pip python-dev build-essential -y
pip install numpy
apt-get install libatlas-base-dev gfortran -y
pip install scipy

apt-get install ipython -y
