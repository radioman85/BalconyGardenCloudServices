# Balcony Garden Cloud Services
This repository containes all required cloud services required for my IoT project. I.e. a webpage, MQTT broker and InfluxDB. Each of them are being set up inside a docker container.

### Web Page Container
This page provides some buttons to control the stepper motor (which open/closes the window of the greenhouse) of the embedded device. It also has some status fields to provide an insight of the embedded systems status.

### MQTT Broker Container
This container contains a mosquitto MQTT broker that enables participants to publish and subscirpt messages over MQTT.

### InfluxDB Container
This container provides a data base to store and also diplay timeline data (e.g. environmental data such temperatrue, pressure, etc.).

Having set it up and running, you will be able to connect to the embedded system of the greenhouse (i.e. sending commands and receiving status updates).

# How to use it
Set up the Docker environment by running the YAML file. Use the following Docker command:

```
docker-compose -f balcony-garden-docker-composition.yml up -d
```

Alternativly you can also run the provided python script, which does the above thing:

```
python setupComposition.py
``` 
(Eventually it's a memorable one-liner compared to the first one)

# About the Yaml-file
If you want to use your own webpage (or an updated one for your purpose) make sure you have 
1. published a docker image in your own docker hub account and
2. update the yaml file by replacing the docker hub address.
For setting up a docker image that contains your webpage, checkout the related repository [BalconyGardenWebPage](https://github.com/radioman85/BalconyGardenWebPage).

# Related Repositories:
- Top Level Repo: [BalconyGarden](https://github.com/radioman85/BalconyGarden)
- Embedded System: [Greenhouse Embedded](https://github.com/radioman85/GreenhouseEmbedded)
- WebPage Development: [BalconyGardenWebPage](https://github.com/radioman85/BalconyGardenWebPage)



