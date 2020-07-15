# Anomaly Detection Prototype

This workshop contains the sample application and machine learning code used for the Continuous Delivery for Machine Learning (CD4ML) and Continuous Intelligence workshop. 

This workshop is based on an existing [CD4ML Workshop](https://github.com/ThoughtWorksInc/cd4ml-workshop).

## Pre-Requisites

In order to run this workshop, you will need:

* A valid Github account
* A working Docker setup with at least 20 GB of space free (if running on Windows, make sure to use Linux containers)

## Tools used in this workshop

* [Python 3.7](https://www.python.org/downloads/release/python-377/)
* [Docker](https://www.docker.com/)
* [Jenkins](https://jenkins.io/)
* EFK Stack, [ElasticSearch](https://www.elastic.co/elasticsearch/), [Fluentd](https://www.fluentd.org/), [Kibana](https://www.elastic.co/kibana) 

We built a simplified solution to a Kaggle problem posted by Corporación Favorita, a large Ecuadorian-based grocery retailer interested in improving their [Sales Forecasting](https://www.kaggle.com/c/favorita-grocery-sales-forecasting/overview) using data. For the purposes of this workshop, we have combined and simplified their data sets, as our goal is not to find the best predictions, but to demonstrate how to implement CD4ML.

## Links to the different components of this scenario

After a successful setup of the environment, the following components are running on your machine:

* [Jenkins](http://localhost:10000/blue)
* [MLFlow](http://localhost:12000)
* [The ML Model](http://localhost:11000)
* [Kibala/fluentD/Elasticsearch](http://localhost:5601/app/kibana)