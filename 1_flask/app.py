from flask import Flask, render_template, jsonify
from gpiozero import InputDevice

app = Flask(__name__)

parkingSpot1 = None
parkingSpot2 = None

occupiedSpots = {}
prevOccupiedSpots = {}


def getParkingDevices():
    global parkingSpot1, parkingSpot2

    if parkingSpot1 is None:
        parkingSpot1 = InputDevice(5)
    if parkingSpot2 is None:
        parkingSpot2 = InputDevice(6)

    return parkingSpot1, parkingSpot2


def updateParkingSpots():
    parkingSpot1, parkingSpot2 = getParkingDevices()
    isOccupied = {}
    isOccupied["spot1"] = not parkingSpot1.is_active
    isOccupied["spot2"] = not parkingSpot2.is_active
    return isOccupied

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/parking-status')
def get_parking_status():
    global prevOccupiedSpots, occupiedSpots
    prevOccupiedSpots = occupiedSpots
    occupiedSpots = updateParkingSpots()
    if(occupiedSpots != prevOccupiedSpots):
        print("Parking Spots have Changed " + str(occupiedSpots))
    return jsonify({
        "spot1": occupiedSpots.get("spot1", False),
        "spot2": occupiedSpots.get("spot2", False)
    })


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
