import threading
import requests
from datetime import datetime, timezone, timedelta

from events.models import VOL

from django.utils import timezone as django_timezone


def set_interval(func, sec):
    def func_wrapper():
        func()
        set_interval(func, sec)  # Appel récursif après chaque exécution de la fonction
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def calcul():
    data_vol()
    logoff_data()
    temps_vol()

set_interval(calcul, 15)

# URL de la base de données de vatsim
vatsim_url = "https://data.vatsim.net/v3/vatsim-data.json"

# Fonction qui cherche les données dans le fichier db de vatsim
def fetch_data():
        response = requests.get(vatsim_url)
        data = response.json()
        return data

def data_vol():
    vatsim_data = fetch_data()

    for data in vatsim_data['pilots']:
        if data.get('callsign').startswith("FBT"):
            callsign = data.get('callsign')
            date_co = data.get('logon_time')
            flight_plan = data.get("flight_plan")

            # Vérifier si un vol avec le même callsign et date_co existe déjà dans la base de données
            existing_vol = VOL.objects.filter(callsign=callsign, date_co=date_co).first()
            if not existing_vol:
                vol = VOL()
                if not flight_plan == None:
                    vol = VOL(callsign=callsign,
                              pilote=data.get('name'),
                              cid=data.get('cid'),
                              depart=flight_plan.get('departure'),
                              destination=flight_plan.get('arrival'),
                              avion=flight_plan.get('aircraft_short'),
                              regime='IFR' if flight_plan.get('flight_rules') == "I" else 'VFR',
                              date_co=date_co)
                    vol.save()

def logoff_data():
    vols = VOL.objects.all()
    vatsim_data = fetch_data()

    for vol in vols:
        if vol.date_logoff is None:
            callsign_in_database = vol.callsign
            callsign_found = False

            for data in vatsim_data['pilots']:
                if data.get('callsign') == callsign_in_database:
                    callsign_found = True
                    break

            if not callsign_found:
                    vol.date_logoff = datetime.now(timezone.utc)
                    vol.save()

def temps_vol():
    vols = VOL.objects.all()

    for vol in vols:
        if vol.temps_co is None:
            if vol.date_logoff is not None and vol.date_co is not None:
                date_logoff = vol.date_logoff.replace(tzinfo=timezone.utc)
                date_co = vol.date_co.replace(tzinfo=timezone.utc)
                elapsed_time = date_logoff - date_co

                # Convert the timedelta to hours, minutes, and seconds
                hours, remainder = divmod(elapsed_time.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)

                # Convert the elapsed time to a timedelta object
                elapsed_time_timedelta = timedelta(hours=hours, minutes=minutes, seconds=seconds)

                # Assign the timedelta to the temps_co field
                vol.temps_co = elapsed_time_timedelta
                vol.save()


def temps_totale():
    vols = VOL.objects.all()
    temps_glob = timedelta()

    for vol in vols:
        if vol.temps_co:
            temps_glob += vol.temps_co

    # Conversion du temps total en heures et minutes
    heures, reste = divmod(temps_glob.seconds, 3600)
    minutes, _ = divmod(reste, 60)

    # Ajout des jours au calcul du temps total en heures et minutes
    heures_total = temps_glob.days * 24 + heures

    # Création d'une chaîne de caractères formatée pour afficher le résultat
    temps_formatte = "{} h {} minutes".format(heures_total, minutes)
    return temps_formatte

def temps_vol_cid(q):
    temps_cid = VOL.objects.filter(cid=q)
    temps_glob = timedelta()

    for vol in temps_cid:
        if vol.temps_co:
            temps_glob += vol.temps_co

    # Conversion du temps total en heures et minutes
    heures, reste = divmod(temps_glob.seconds, 3600)
    minutes, _ = divmod(reste, 60)

    # Ajout des jours au calcul du temps total en heures et minutes
    heures_total = temps_glob.days * 24 + heures

    # Création d'une chaîne de caractères formatée pour afficher le résultat
    temps_formatte = "{} h {} minutes".format(heures_total, minutes)
    return temps_formatte