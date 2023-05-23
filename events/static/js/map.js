const vatsim_url = "https://data.vatsim.net/v3/vatsim-data.json";

function fetchData(){
  fetch(vatsim_url)
    .then(response => response.json())
    .then(data => {
      let tableau_long = [];
      let tableau_lat = [];
      let tableau_dep = [];
      let tableau_arr = [];
      let tableau_callsign = [];
      let tableau_aircraft = [];
      let tableau_heading = [];
      let tableau_speed = [];
      let tableau_pilote = [];
      let tableau_rules = [];
      let tableau_status = [];
      let tableau_fpl_altitude = [];
      let tableau_altitude = [];

      data.pilots.forEach(pilot => {
        if (pilot.callsign.startsWith('DLH')) {
          tableau_long.push(pilot.longitude);
          tableau_lat.push(pilot.latitude);
          tableau_callsign.push(pilot.callsign);
          tableau_heading.push(pilot.heading);
          tableau_speed.push(pilot.groundspeed);
          tableau_pilote.push(pilot.name);
          tableau_altitude.push(pilot.altitude)

          if (pilot.flight_plan == null) {
              tableau_dep.push("No FPL")
              tableau_arr.push("")
              tableau_aircraft.push("")
              tableau_rules.push("")
              tableau_fpl_altitude.push("")
          }else{
              tableau_dep.push(pilot.flight_plan.departure)
              tableau_arr.push(pilot.flight_plan.arrival)
              tableau_aircraft.push(pilot.flight_plan.aircraft_short)
              tableau_rules.push(pilot.flight_plan.flight_rules)
              tableau_fpl_altitude.push(pilot.flight_plan.altitude)
          }
        }
      });

      let tableau_rules_T = [];
      tableau_status = checkstatus(tableau_status, tableau_speed, tableau_fpl_altitude, tableau_altitude)
      tableau_rules_T = rules_transform(tableau_rules)
      initMap(tableau_lat, tableau_long, tableau_dep, tableau_arr, tableau_callsign, tableau_aircraft, tableau_heading, tableau_speed);
      table_vol(tableau_callsign, tableau_aircraft, tableau_dep, tableau_arr, tableau_pilote, tableau_rules_T, tableau_status);
      nb_pilot(tableau_callsign);
    })
    .catch(error => {
      console.error("Une erreur s'est produite lors de la récupération des données:", error);
    });
}

var mymap = null;
var markers = [];
window.onload = fetchData;

function autoActualisation() {
  fetchData();
}

setInterval(autoActualisation, 15000);

function initMap(latitude, longitude, depart, arrive, callsign, aircraft, heading, speed) {
  if (mymap === null) {
    mymap = L.map('map').setView([48.8566, 2.3522], 4);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '© OpenStreetMap contributors',
      filter: 'grayscale'
    }).addTo(mymap);

    /*Legend specific*/
    var legend = L.control({ position: "bottomleft" });

    legend.onAdd = function(mymap) {
      var div = L.DomUtil.create("div", "legend");
      div.innerHTML += '<h4>Légende</h4><br>';
      div.innerHTML += '<div class="legend-item"><img src="/static/asset/icon.png"><span>Avion en vol</span></div>';
      div.innerHTML += '<div class="legend-item"><img src="/static/asset/icon_ground.png"><span>Avion au sol</span></div>';
      div.innerHTML += "<div class='legend-item'>La carte et le tableau s'actualisent automatiquement toutes les 15 secondes </div>";
      return div;
    };
    

    legend.addTo(mymap);
  } else {
    for (var i = 0; i < markers.length; i++) {
      mymap.removeLayer(markers[i]);
    }
    markers = [];
  }

  for (var i = 0; i < latitude.length; i++) {
    var popup = callsign[i] + '<br>' + "Depart: " + depart[i] + '<br>' + "Destination: " + arrive[i] + '<br>' + "Appareil: " + aircraft[i];

    if (speed[i] < 40){
      markers[i] = new L.marker([latitude[i], longitude[i]], {
        icon: IconSol,
        rotationAngle: heading[i],
      });
    }else{
        markers[i] = new L.marker([latitude[i], longitude[i]], {
        icon: IconVol,
        rotationAngle: heading[i],
      });
    }
    markers[i].bindPopup(popup);
    markers[i].addTo(mymap);
}
}

var IconVol = L.icon({
  iconUrl: "/static/asset/icon.png",
  iconSize: [16, 16],
});

var IconSol = L.icon({
  iconUrl: "/static/asset/icon_ground.png",
  iconSize: [16, 16],
});

function nb_pilot(tableau_callsign)
{
    var nb_pilots = 0
    nb_pilots = tableau_callsign.length
    document.getElementById("entete").innerHTML = "Tableau des vols (" + nb_pilots + " en cours)";
}

function checkstatus(status, speed, fpl_altitude, altitude) {
  for (var i = 0; i < speed.length; i++) {
    if (speed[i] === 0) {
      status[i] = "A l'arret";
    } else if (speed[i] > 0 && speed[i] < 40) {
      status[i] = "Au roulage";
    } else if (altitude[i] > fpl_altitude[i] - 1000) {
      status[i] = "En croisière";
    } else {
      status[i] = "En montée / descente";
    }
  }
  return status;
}

function rules_transform(rules){
  for(var i = 0; i < rules.length; i++){
    if (rules[i] == "I"){
      rules[i] = "IFR"
    }else if(rules[i] == "V"){
      rules[i] = "VFR"
    }
  }
  return rules
}

function table_vol(callsign, aircraft, dep, arr, pilote, rules, status) {
  var tableau = document.getElementById("vol");
  
  // Supprimer les lignes existantes du tableau
  while (tableau.firstChild) {
    tableau.removeChild(tableau.firstChild);
  }
  
  // Création du caption
  var caption = document.createElement("caption");
  caption.id = "entete";
  
  tableau.appendChild(caption);
  
  var nouvelleLigne = document.createElement("tr");
  var cellulesEnTete = ["Callsign", "Pilote", "Depart", "Destination", "Appareil", "Type de vol", "Status"];
  
  // Création des cellules d'en-tête
  for (var i = 0; i < cellulesEnTete.length; i++) {
    var celluleEnTete = document.createElement("th");
    celluleEnTete.innerHTML = cellulesEnTete[i];
    nouvelleLigne.appendChild(celluleEnTete);
  }
  
  tableau.appendChild(nouvelleLigne);
  
  // Ajout des données aux lignes du tableau
  for(var i = 0; i < callsign.length; i++) {
    var nouvelleLigne = document.createElement("tr");
    var cellules = [callsign[i], pilote[i], dep[i], arr[i], aircraft[i], rules[i], status[i]];
    
    // Création des cellules de données
    for (var j = 0; j < cellules.length; j++) {
      var cellule = document.createElement("td");
      cellule.innerHTML = cellules[j];
      nouvelleLigne.appendChild(cellule);
    }
    
    tableau.appendChild(nouvelleLigne);
  }
}

