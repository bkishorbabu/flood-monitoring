// Simulated real-time data (replace with actual IoT sensor data)
let waterLevel = 0;

function updateWaterLevel() {
    // Simulated data update
    waterLevel += Math.random() * 10;
    document.getElementById('water-level-value').textContent = waterLevel + ' cm';

    // Check for flood conditions (set your threshold)
    if (waterLevel > 50) {
        document.getElementById('warning-message').textContent = 'Flood warning! Evacuate the area.';
        document.getElementById('flood-warning').classList.add('warning-active');
    } else {
        document.getElementById('warning-message').textContent = 'No flood warnings at the moment.';
        document.getElementById('flood-warning').classList.remove('warning-active');
    }
}

setInterval(updateWaterLevel, 5000); // Update data every 5 seconds
