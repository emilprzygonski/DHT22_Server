let live_temp = document.getElementById("live_temp");

async function makeGetRequest(host) {
  const response = await fetch(host);
  const data = await response.json();
  return data;
}

async function updateData() {
  const valueFromServer = await makeGetRequest("data");

  console.log(valueFromServer);
  live_temp.innerHTML = valueFromServer.series[0].at(-1);
  setTimeout(async () => {
    await updateData();
  }, 1000);
}
