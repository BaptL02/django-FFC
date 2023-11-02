//URL de la base de données de vatsim
const vatsim_url = "https://data.vatsim.net/v3/vatsim-data.json";

//Fonction qui cherche les données dans le fichier db de vatsim
function fetchData() {
  fetch(vatsim_url)
    .then(response => response.json())
    .then(data => {
      //Définition du stockage des données
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
      let marker_state = [];
      let tableau_CID = [];

      //Parcours la liste complète des pilotes présents sur le réseau
      data.pilots.forEach(pilot => {
        if (pilot.callsign.startsWith('FBT') || pilot.callsign.startsWith('BREAD')) { //Si le callsign commence par FBT alors
          //Stockage des données qui ne sont pas inscrites dans le plan de vol envoyé par le pilote
          tableau_long.push(pilot.longitude);
          tableau_lat.push(pilot.latitude);
          tableau_callsign.push(pilot.callsign);
          tableau_heading.push(pilot.heading);
          tableau_speed.push(pilot.groundspeed);
          tableau_pilote.push(pilot.name);
          tableau_altitude.push(pilot.altitude)
          tableau_CID.push(pilot.cid)

          if (pilot.flight_plan == null) { // Si le plan de vol est null (pilote n'a rien envoyé) alors il écrit une chaîne vide dans les cases ( évite les bugs )
            tableau_dep.push("No FPL")
            tableau_arr.push("")
            tableau_aircraft.push("")
            tableau_rules.push("")
            tableau_fpl_altitude.push("")
          } else { //Sinon il écrit les valeurs que l'on a besoin relative au plan de vol 
            tableau_dep.push(pilot.flight_plan.departure)
            tableau_arr.push(pilot.flight_plan.arrival)
            tableau_aircraft.push(pilot.flight_plan.aircraft_short)
            tableau_rules.push(pilot.flight_plan.flight_rules)
            tableau_fpl_altitude.push(pilot.flight_plan.altitude)
          }
        }
      });

      let tableau_rules_T = []; //Initialise le tableau des règles de vol modifié. (Fait pour que le "I" du json se transforme en IFR)
      tableau_status = checkstatus(tableau_status, tableau_speed, tableau_fpl_altitude, tableau_altitude) //Rempli le tableau relatif au status de l'avion
      tableau_rules_T = rules_transform(tableau_rules) //Change le "I" en "IFR", same pour le VFR
      initMap(tableau_lat, tableau_long, tableau_dep, tableau_arr, tableau_callsign, tableau_aircraft, tableau_heading, tableau_speed, marker_state, tableau_altitude, tableau_CID); //Lance initmap (affichage map)
      table_vol(tableau_callsign, tableau_aircraft, tableau_dep, tableau_arr, tableau_pilote, tableau_rules_T, tableau_status); //Lance la conception et l'affichage du tableau
      nb_pilot(tableau_callsign); //Récupere le nombre de pilote en FBT
    })
    .catch(error => {
      console.error("Une erreur s'est produite lors de la récupération des données:", error); //Erreur console
    });
}

var mymap = null; //Crée une variable qui contiendra la map
var markers = []; //Crée un tableau qui contiendra les markers à mettre sur la map (ici les avions)
window.onload = fetchData; //Lance la recherche des données au chargement de la page

setInterval(fetchData, 15000); // Actualise la map toutes les 15 secondes (fréquence d'actualisation du json de vatsim)

//Fonction d'affichage de la map
function initMap(latitude, longitude, depart, arrive, callsign, aircraft, heading, speed, marker_state, altitude, CID) {

  if (mymap === null) { //Si la map est créée 
    mymap = L.map('map').setView([48.8566, 2.3522], 4); //Définit la position de la map au chargement de la page (ici centrée sur Paris avec un zoom de 4 (permettant de voir l'europe))

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { //On se sert de openstreetmap 
      attribution: '© OpenStreetMap contributors', //On crédite ceux qui nous ont facilité le travail
    }).addTo(mymap); //on ajoute le layer de la carte à la variable map

    /*Legend specific*/
    var legend = L.control({ position: "bottomleft" }); //On crée une légende en bas à gauche

    legend.onAdd = function (mymap) { //On crée la légende avec différents paramètres
      var div = L.DomUtil.create("div", "legend");
      div.innerHTML += '<h4>Légende</h4><br>';
      div.innerHTML += '<div class="legend-item"><img src="/static/asset/icon.png"><span>Avion en vol</span></div>';
      div.innerHTML += '<div class="legend-item"><img src="/static/asset/icon_ground.png"><span>Avion au sol</span></div>';
      div.innerHTML += "<div class='legend-item'>La carte et le tableau s'actualisent automatiquement toutes les 15 secondes </div>";
      return div;
    };

    legend.addTo(mymap); //On ajoute la légende à la map 

  } else {
    for (var i = 0; i < markers.length; i++) {
      mymap.removeLayer(markers[i]);
      markerClickCallback_del(i);

      if (marker_state[i] === 0) {
        markerClickCallback_add(e, depart[i], arrive[i], i); // Passer l'index en tant qu'argument supplémentaire
        marker_state[i] = 1;
      }
    }
    markers = [];
  }

  for (var i = 0; i < latitude.length; i++) {
    var popup = callsign[i] + '<br>' + depart[i] + " | " + arrive[i] + '<br>' + + altitude[i] + " fts" + ' | ' + speed[i] + ' kts' + '<br>' + aircraft[i];
    if (speed[i] < 40) {
      markers[i] = new L.marker([latitude[i], longitude[i]], {
        icon: IconSol,
        rotationAngle: heading[i],
      });
    } else {
      markers[i] = new L.marker([latitude[i], longitude[i]], {
        icon: IconVol,
        rotationAngle: heading[i],
      });
    }

    marker_state[i] = 0; // Définir marker_state[i] pour chaque marqueur comme 0 initialement

    markers[i].bindPopup(popup);
    markers[i].addTo(mymap);

    markers[i].on('click', (function (departValue, arriveValue, index) {
      return function (e) {
        if (marker_state[index] === 0) {
          markerClickCallback_add(e, departValue, arriveValue, index); // Passer l'index en tant qu'argument supplémentaire
          marker_state[index] = 1;
        } else {
          markerClickCallback_del(index); // Passer l'index en tant qu'argument supplémentaire
          marker_state[index] = 0;
        }
      };
    })(depart[i], arrive[i], i));
  }
}

var traits_togo = []; // Stocker les instances de trait dans un tableau
var traits_flown = []; // Stocker les instances de trait dans un tableau

// Fonction de gestion du clic sur un marqueur
async function markerClickCallback_add(e, depart, arrive, index) {
  coordonnees = await airportCoor(depart, arrive);
  airportcoor_dep = L.latLng([coordonnees[0], coordonnees[1]]);
  airportcoor_arr = L.latLng([coordonnees[2], coordonnees[3]]);

  // Récupère les coordonnées du marqueur cliqué
  var markerLatLng = e.latlng;

  // Crée un trait à partir du marqueur jusqu'à une nouvelle position
  var trait_togo = L.polyline([markerLatLng, airportcoor_arr], {
    weight: 3, // Épaisseur du trait (3 pixels)
    color: '#2483c5', // Couleur du trait (#2483c5)
    dashArray: '10, 10' // Motif de pointillé (10 pixels de ligne, 10 pixels d'espace)
  });

  // Crée un trait à partir du marqueur jusqu'à une nouvelle position
  var trait_flown = L.polyline([airportcoor_dep, markerLatLng], {
    weight: 3, // Épaisseur du trait (3 pixels)
    color: '#2483c5', // Couleur du trait (#2483c5)
  });

  trait_togo.addTo(mymap); //Ajoute le trait à la map 
  trait_flown.addTo(mymap); //Ajoute le trait à la map   
  traits_togo[index] = trait_togo; // Stocker l'instance de trait dans le tableau des traits
  traits_flown[index] = trait_flown;
}

function markerClickCallback_del(index) {
  var trait_togo = traits_togo[index]; // Récupérer l'instance de trait à supprimer
  var trait_flown = traits_flown[index]

  if (trait_togo) {
    mymap.removeLayer(trait_togo); // Supprimer le trait de la carte
    mymap.removeLayer(trait_flown); // Supprimer le trait de la carte
    traits_togo[index] = undefined; // Définir l'élément du tableau à undefined
    traits_flown[index] = undefined; // Définir l'élément du tableau à undefined
  }
}

function extractAirportCoord(icaoCode, fileContent) {
  const lines = fileContent.split('\n');

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();

    if (line.startsWith(icaoCode)) {
      const parts = line.split('\t');

      const latitude = parseFloat(parts[1]);
      const longitude = parseFloat(parts[2]);
      return { latitude, longitude };

    }
  }
  return null; // Retourner null si le code OACI n'est pas trouvé
}

function airportCoor(depart, arrive) {
  var depart_lat = 0
  var depart_long = 0
  var arrive_lat = 0
  var arrive_long = 0
  return fetch('static/js/icao.txt')
    .then(response => response.text())
    .then(fileContent => {
      console.log(depart)
      const airportDepCoor = extractAirportCoord(depart, fileContent);
      const airportArrCoor = extractAirportCoord(arrive, fileContent);

      if (airportDepCoor) {
        depart_lat = airportDepCoor.latitude;
        depart_long = airportDepCoor.longitude;
      } else {
        console.log('Aéroport de départ non trouvé.');
      }

      if (airportArrCoor) {
        arrive_lat = airportArrCoor.latitude;
        arrive_long = airportArrCoor.longitude;
      } else {
        console.log("Aéroport d'arrivée non trouvé.");
      }

      return [depart_lat, depart_long, arrive_lat, arrive_long];
    });
}

function createPolygon(depart_lat, depart_long, latitude, longitude, arrive_lat, arrive_long) {
  var polygon = L.polygon([
    [depart_lat, depart_long],
    [latitude, longitude],
    [arrive_lat, arrive_long]
  ]).addTo(mymap);
}

var IconVol = L.icon({
  iconUrl: "/static/asset/icon.png",
  iconSize: [16, 16],
  iconAnchor: [8, 8],
});

var IconSol = L.icon({
  iconUrl: "/static/asset/icon_ground.png",
  iconSize: [16, 16],
  iconAnchor: [8, 8],
});

function nb_pilot(tableau_callsign) {
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

function rules_transform(rules) {
  for (var i = 0; i < rules.length; i++) {
    if (rules[i] == "I") {
      rules[i] = "IFR"
    } else if (rules[i] == "V") {
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
  for (var i = 0; i < callsign.length; i++) {
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

