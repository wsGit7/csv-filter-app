const API = "https://csv-filter-app.onrender.com/filter";

async function filter() {
  const params = new URLSearchParams();

  const brand = document.getElementById("brand").value.trim();
  const speed = document.getElementById("speed").value.trim();
  const number = document.getElementById("number").value.trim();

  if (brand !== "") params.append("brand", brand);
  if (speed !== "") params.append("speed", speed);
  if (number !== "") params.append("number", number);

  const res = await fetch(API + "?" + params.toString());
  const data = await res.json();

  const table = document.getElementById("results");
  table.innerHTML = "<tr><th>brand</th><th>speed</th><th>number</th></tr>";

  data.forEach(row => {
    table.innerHTML += `<tr><td>${row.brand}</td><td>${row.speed}</td><td>${row.number}</td></tr>`;
  });
}
