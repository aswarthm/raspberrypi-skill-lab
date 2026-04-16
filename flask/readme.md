# Parking Management System (Flask Web App)

This project demonstrates a parking spot monitoring system using Raspberry Pi GPIO sensors and Flask web framework.

## Installation

First, navigate into the project directory:

```bash
cd parking-flask
```

Setup a virtual environment:

```bash
python -m venv venv --system-site-packages
. venv/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

## Run the application

Finally, run the application:

```bash
python app.py
```

The web interface will be available at `http://localhost:5000` (or `http://<raspberry-pi-ip>:5000` if accessed from another machine).

## Features

- Real-time GPIO sensor monitoring for parking spot occupancy
- Flask web server with REST API for parking status
- Automatic updates only when parking status changes
- Simple HTML interface with live status display
- Color-coded display (red = occupied, green = available)
- Continuous monitoring with 1-second polling interval
