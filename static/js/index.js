function makeRequest() {
    // get form data as json
    const submitButton = document.getElementById('predict-button');
    submitButton.addEventListener('click', async (e) => {
        e.preventDefault();
        document.getElementById('results').innerHTML = `<div class="loading loading-lg"></div>`;
        const formData = new FormData(document.getElementById('predict-form'));
        const data = Object.fromEntries(formData.entries());
        for (let key in data) {
            data[key] = [parseFloat(data[key])];
        }
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        });
        const result = await response.json();
        document.getElementById('results').innerHTML = `
            <img src="static/images/${result['prediction']}.jpg" width="250px;" height="250px;" alt="prediction" />
            <br />
            <b>${result['prediction']}</b>
        `;
    });
}

window.addEventListener('DOMContentLoaded', makeRequest);
