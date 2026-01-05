let demandChart;

document.getElementById('loadBtn').addEventListener('click', async () => {
    const response = await fetch('http://127.0.0.1:8000/predict');
    const data = await response.json();

    const ctx = document.getElementById('forecastChart').getContext('2d');

    if (demandChart) demandChart.destroy();

    demandChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: `Demand in ${data.unit}`,
                data: data.values,
                borderColor: '#2ecc71',
                backgroundColor: 'rgba(46, 204, 113, 0.2)',
                fill: true,
                tension: 0.4
            }]
        }
    });
});