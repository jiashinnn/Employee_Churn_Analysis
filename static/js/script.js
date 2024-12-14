// Function to clear form inputs and the prediction result
function clearFormAndResult() {
    // Reset the form inputs
    const form = document.getElementById("predictionForm");
    if (form) {
        form.reset(); // Resets all the input fields in the form
    }

    // Clear the prediction result
    const resultDiv = document.getElementById("predictionResult");
    if (resultDiv) {
        resultDiv.innerHTML = ""; // Clear the content of the result div
        resultDiv.style.display = "none"; // Hide the result div
    }
}
