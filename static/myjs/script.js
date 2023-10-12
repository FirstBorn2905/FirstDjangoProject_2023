var el = document.getElementById("wrapper");
var toggleButton = document.getElementById("menu-toggle");

toggleButton.onclick = function () {
    el.classList.toggle("toggled");
};

// Script de Apache Echarts
// const getOptionChart = async () => {
//     try {
//         const response = await fetch("http://127.0.0.1:8000/ventas/chart/");
//         return await response.json();
//     } catch (ex) {
//         alert(ex);
//     }
// };

// const initChart = async () => {
//     // Se inicia el grafico
//     const myChart = echarts.init(document.getElementById("chart"), 'dark');

//     myChart.setOption(await getOptionChart());
//     myChart.resize(); 
// };

// window.addEventListener("load", async () => {
//     await initChart();
// });

// Script de Chartjs
