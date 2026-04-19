# HiveMQ MQTT Client

This project demonstrates a parking spot monitoring system using Raspberry Pi GPIO sensors and HiveMQ Cloud MQTT broker.

## Installation

First, navigate into the project directory:

```bash
cd 3_mqtt
```

Setup a virtual environment

```bash
python -m venv venv --system-site-packages
. venv/bin/activate
```

Install requirements

```bash
pip install paho-mqtt
```

## Configuration

Before running the application, you need to configure your HiveMQ Cloud credentials:

1. Sign up for [HiveMQ Cloud](https://www.hivemq.cloud/).
2. Create a cluster and note the broker address.
3. Open `hivemq.py` and update the following variables:
   - `hive_mq_cloud`: Your HiveMQ Cloud broker address
   - `username`: Your MQTT username
   - `password`: Your MQTT password

## Run the application

Finally, run the application:

```bash
python hivemq.py
```

## Features

- Real-time GPIO sensor monitoring for parking spot occupancy
- HiveMQ Cloud MQTT integration for IoT communication
- Automatic updates only when parking status changes
- TLS secure connection to MQTT broker
- Button topic subscription for remote control
- Continuous monitoring with 1-second polling interval
