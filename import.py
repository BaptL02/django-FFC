import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet_site.settings')
django.setup()
print('Setup complete')

from events.models import VOL    

def import_data():
    fichier_excel = "Classeur1.xlsx"
    sheet_name = "Feuil1"

    try:
        df = pd.read_excel(fichier_excel, sheet_name=sheet_name)
        print(df.head())
        print('Démarrage import Data')
        
        # Convert 'temps_co' column to string in 'hh:mm:ss' format
        df['temps_co'] = df['temps_co'].astype(str)
        
        # Convert 'temps_co' column to timedelta format
        df['temps_co'] = pd.to_timedelta(df['temps_co'])
        
        # Correct the 'date_co' column to the required format 'YYYY-MM-DD HH:MM'
        df['date_co'] = pd.to_datetime(df['date_co'], format='%d/%m/%Y à %H:%M').dt.strftime('%Y-%m-%d %H:%M')
        
        donnees_a_inserer = df.to_dict(orient='records')
        VOL.objects.bulk_create([VOL(**donnees) for donnees in donnees_a_inserer])
        print('Data inserted successfully!')
        
    except Exception as e:
        print(f"Error occurred: {e}")

def import_CID():
    fichier_excel = "Classeur1.xlsx"
    sheet_name = "Feuil2"

    try:
        df = pd.read_excel(fichier_excel, sheet_name=sheet_name)
        print(df.head())
        print('Démarrage import CID')
        
        donnees_a_inserer = df.to_dict(orient='records')    
        vols = VOL.objects.all()

        for vol in vols:
            for donnee in donnees_a_inserer:
                if vol.pilote == donnee['Nom']:
                    vol.cid = donnee['CID']
                    vol.save()

        print('CID inserted successfully!')

    except Exception as e:
        print(f"Error occurred: {e}")

import_data()
import_CID()
