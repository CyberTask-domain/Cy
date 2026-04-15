// client-side functionality for the web app

// Function to update the current date and time
function updateDateTime() {
    const now = new Date();
    const formattedDate = now.toISOString().slice(0, 19).replace('T', ' ');
    document.getElementById('currentDateTime').innerText = formattedDate;
}

// Update the date and time every second
setInterval(updateDateTime, 1000);
// Call it once to set initial value
updateDateTime();
