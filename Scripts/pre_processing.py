import pandas as pd
import ijson
import os
from datetime import datetime, timedelta

# --- 1. CONFIGURATION ---
CHEMIN_JSON = r"C:\Users\berri\Desktop\Projet_PulsEvent\evenements-publics-openagenda.json"
VILLE_CIBLE = "Paris" 
LIMITE_EVENEMENTS = 300 

def executer_nettoyage_consigne(chemin, ville_recherchee):
    print(f" Application des filtres : {ville_recherchee} + Moins d'un an...")
    
    # CONSIGNE : Moins d'un an (on prend les évènements depuis 1 an jusqu'à aujourd'hui)
    un_an_en_arriere = datetime.now() - timedelta(days=365)
    
    resultats = []

    try:
        with open(chemin, 'r', encoding='utf-8') as f:
            objets = ijson.items(f, 'item')
            
            for ev in objets:
                ville_actuelle = str(ev.get('location_city', '')).strip().lower()
                
                # FILTRE 1 : Périmètre géographique
                if ville_recherchee.lower() in ville_actuelle:
                    
                    # FILTRE 2 : Événements de moins d'un an
                    date_fin_str = ev.get('lastdate_end')
                    try:
                        # tz_localize(None) permet de comparer des dates sans fuseaux horaires
                        date_fin = pd.to_datetime(date_fin_str).tz_localize(None)
                        
                        if date_fin >= un_an_en_arriere:
                            resultats.append({
                                'Titre': ev.get('title_fr', 'Sans titre'),
                                'Lieu': ev.get('location_name', 'Lieu inconnu'),
                                'Adresse': ev.get('location_address', ''),
                                'Ville': ev.get('location_city', 'Paris'),
                                # On assure une valeur par défaut si None
                                'Description': ev.get('description_fr') or 'Pas de description',
                                'Horaires': ev.get('daterange_fr', 'Non précisé'),
                            })
                    except:
                        continue

                if len(resultats) >= LIMITE_EVENEMENTS:
                    break

    except Exception as e:
        print(f" Erreur lors de la lecture : {e}")
        return

    df = pd.DataFrame(resultats)

    if not df.empty:
        # --- CRÉATION DU TEXTE POUR RAG (Version sécurisée) ---
        # str(x['Description']) empêche le crash si la donnée est un float/NaN
        df['text_for_rag'] = df.apply(
            lambda x: (f"ÉVÉNEMENT : {x['Titre']}. "
                       f"LIEU : {x['Lieu']} ({x['Adresse']}, {x['Ville']}). "
                       f"QUAND : {x['Horaires']}. "
                       f"INFOS : {str(x['Description'])[:500]}"), axis=1
        )

        df.to_csv("paris_events_ready.csv", index=False, encoding='utf-8')
        print(f" Étape validée : {len(df)} événements sauvegardés.")
    else:
        print(" Aucun événement trouvé avec ces filtres.")

if __name__ == "__main__":
    executer_nettoyage_consigne(CHEMIN_JSON, VILLE_CIBLE)
