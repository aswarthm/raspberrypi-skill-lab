import firebase_admin
from firebase_admin import db
from gpiozero import InputDevice
from time import sleep


credObj = firebase_admin.credentials.Certificate('./key.json')

ref = db.reference("/")
defaultApp = firebase_admin.initialize_app(credObj, {
    'databaseURL': "firebase_url"
})
# data = ref.get() # Gets full firebase

parkingSpot1 = InputDevice(5)
parkingSpot2 = InputDevice(6)

occupiedSpots = {}
prevOccupiedSpots = {}

def updateParkingSpots():
    isOccupied = {}

    isOccupied["spot1"] = not parkingSpot1.is_active
    isOccupied["spot2"] = not parkingSpot2.is_active

    return isOccupied

def writeToFirebase(occupiedSpots):
    ref.update(occupiedSpots)

while True:
    prevOccupiedSpots = occupiedSpots
    occupiedSpots = updateParkingSpots()
    if (occupiedSpots != prevOccupiedSpots):
        writeToFirebase(occupiedSpots)
        print("Parking Spots have Changed " + str(occupiedSpots))
    sleep(1)
