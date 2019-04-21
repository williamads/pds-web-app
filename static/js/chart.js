function drawChart1(myData) {
    var ctx = document.getElementById('chart1');
    var scatterChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Signal Input',
                backgroundColor: "#008000",
                data: myData 
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom'
                }]
            }
        }
    });
}
function drawConvolutionChart(myData) {
    var ctx = document.getElementById('convolution-chart');
    var scatterChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Signal Input',
                backgroundColor: "#008000",
                data: myData 
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom'
                }]
            }
        }
    });
}