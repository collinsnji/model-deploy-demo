function makeRequest() {
    // get form data as json
    const submitButton = document.getElementById('predict-button');
    submitButton.addEventListener('click', async (e) => {
        e.preventDefault();
        const formData = new FormData(document.getElementById('predict-form'));
        const data = Object.fromEntries(formData.entries());
        for (let key in data) {
            data[key] = [parseFloat(data[key])];
        }
        console.log(data);
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        });
        const result = await response.json();
        console.log(result);
        document.getElementById('results').innerHTML = `<b>Prediction: ${result['prediction']}</b>`;
    });
}

window.addEventListener('DOMContentLoaded', makeRequest);
