import { initializeApp } from "https://www.gstatic.com/firebasejs/9.9.3/firebase-app.js";
import { get, ref, getDatabase, child, onValue } from "https://www.gstatic.com/firebasejs/9.9.3/firebase-database.js";

const firebaseConfig = {
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
const dbRef = ref(db);

function getParkingStatus() {
  onValue(dbRef, (snapshot) => {
    const data = snapshot.val();

    if (data) {
      const spot1Status = data.spot1;
      const spot2Status = data.spot2;

      updateSpotStatus("spot1", spot1Status);
      updateSpotStatus("spot2", spot2Status);
    }
  });
}

function updateSpotStatus(spotId, isOccupied) {
  const statusElement = document.getElementById(spotId);
  console.log(isOccupied)

  if (isOccupied === true) {
    statusElement.textContent = "Occupied";
    statusElement.style.backgroundColor = "#ffcccc";
  } else if(isOccupied === false) {
    statusElement.textContent = "Available";
    statusElement.style.backgroundColor = "#ccffcc";
  }
}

getParkingStatus();
