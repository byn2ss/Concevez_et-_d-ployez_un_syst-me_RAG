import pandas as pd
from datetime import datetime, timedelta

def test_qualite_donnees():
    print(" Lancement des tests unitaires sur les données...")
    df = pd.read_csv("paris_events_ready.csv")
    
    # --- 1. Test Géographique ---
    # On cherche la colonne qui contient la ville (elle peut s'appeler 'location_city' ou 'ville')
    col_ville = 'location_city' if 'location_city' in df.columns else 'ville'
    
    if col_ville in df.columns:
        villes_hors_paris = df[df[col_ville] != 'Paris']
        assert len(villes_hors_paris) == 0, f"Erreur: {len(villes_hors_paris)} événements ne sont pas à Paris !"
        print(f" Test Géo : Tous les événements sont bien à Paris (colonne utilisée : '{col_ville}').")
    else:
        print(" Attention : Colonne de ville non trouvée, test géo sauté.")

    # --- 2. Test Temporel (Moins d'un an) ---
    un_an_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    col_date = 'date_start' if 'date_start' in df.columns else 'date'
    
    if col_date in df.columns:
        # On s'assure que la colonne est bien au format date
        df[col_date] = pd.to_datetime(df[col_date]).dt.strftime('%Y-%m-%d')
        dates_trop_vieux = df[df[col_date] < un_an_ago]
        assert len(dates_trop_vieux) == 0, f"Erreur: {len(dates_trop_vieux)} événements datent de plus d'un an !"
        print(f" Test Date : Tous les événements ont moins d'un an (colonne utilisée : '{col_date}').")
    else:
        print(" Attention : Colonne de date non trouvée, test temporel sauté.")

    # --- 3. Test de Structure ---
    # C'est la colonne la plus importante du Chatbot
    assert 'text_for_rag' in df.columns, "Erreur: La colonne 'text_for_rag' est manquante !"
    print("Test Structure : La colonne 'text_for_rag' est présente.")

    print("\n TOUS LES TESTS SONT PASSÉS AVEC SUCCÈS !")

if __name__ == "__main__":
    test_qualite_donnees()
