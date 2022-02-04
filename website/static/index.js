// require('chartist-plugin-legend');
console.log("working");

// var temperature = [];
// var humidity = [];
// var labels = [];

var data = {
  labels: [],
  series: [[], []],
};

var options = {
  fullWidth: true,
  chartPadding: {
    right: 40,
    left: 40,
    top: 40,
    bottom: 100,
  },
  showPoint: false,
  showArea: true,
  high: 80,
  low: 0,
  axisX: {
    labelInterpolationFnc: function skipLabels(value, index) {
      return index % 15 === 0 ? value : null;
    },
  },
  axisY: {
    scaleMinSpace: 25,
    position: "dual",
  },
  // plugins: [
  //   Chartist.plugins.legend({
  //     legendNames: ["Custom title", "Another one"],
  //     position: "bottom",
  //   }),
  // ],

  // scales: {
  //   y: { position: "start" },
  //   y1: { position: "right" },
  // },
  // labelInterpolationFnc: Chartist.noop,
};

var chart = new Chartist.Line(".ct-chart", data, options);

async function updateData() {
  const valueFromServer = await makeGetRequest("data");
  let live_time = document.getElementById("live_time");
  let live_temp = document.getElementById("live_temp");
  let live_hum = document.getElementById("live_hum");

  // console.log(valueFromServer);

  var last_index = valueFromServer.series[0].length - 1

  live_time.innerHTML  = valueFromServer.labels[last_index];
  live_temp.innerHTML  = valueFromServer.series[0][last_index];
  live_hum.innerHTML  = valueFromServer.series[1][last_index];

  // alert(live_hum.innerHTML);


  chart.update(valueFromServer);

  setTimeout(async () => {
    await updateData();
  }, 1000);
}

updateData().then((e) => {
  console.log("init done");
});

async function makeGetRequest(host) {
  const response = await fetch(host);
  const data = await response.json();
  return data;
}

// function updateChart(raw_data, length) {
//   if (tempSeries.length >= length) {
//     tempSeries.shift(); //usuwa pierwszą rzecz z array
//     humSeries.shift(); //usuwa pierwszą rzecz z array
//     timeSeries.shift();
//   }
//   tempSeries.push(raw_data.val_temp);
//   humSeries.push(raw_data.val_hum);
//   timeSeries.push(raw_data.time);

//   chart.update(data);
// }

// function getData() {
//   return new Promise((resolve, reject) => {
//     fetch("http://10.0.1.207:5000/data")
//       .then((response) => response.json())
//       .then((data) => {
//         resolve(data);
//       })
//       .catch((err) => {
//         reject(err);
//       });
//     //.then(data => )
//   });
// }

// updateChart(chart, data, getData(20), 10);
