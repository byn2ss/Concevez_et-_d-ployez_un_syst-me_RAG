import os
from langchain_mistralai import ChatMistralAI
from langchain_community.vectorstores import FAISS
from langchain_mistralai import MistralAIEmbeddings
from langchain.chains import RetrievalQA

# --- 1. CONFIGURATION ---
# Remplace par ta vraie clé API Mistral
MISTRAL_API_KEY = "BWIRQNrANwF4FU2ThqL4Vi5gvgVRYAS2" 
os.environ["MISTRAL_API_KEY"] = MISTRAL_API_KEY

def lancer_chatbot():
    print(" Initialisation du Chatbot Puls-Events...")

    # 2. CHARGEMENT DU "CERVEAU" (L'index créé à l'étape 3)
    # On utilise le même modèle d'embedding pour que l'IA comprenne la question
    embeddings = MistralAIEmbeddings(model="mistral-embed")
    
    # On charge les fichiers FAISS et PKL depuis ton dossier local
    vector_db = FAISS.load_local(
        "faiss_index_paris", 
        embeddings, 
        allow_dangerous_deserialization=True # Nécessaire pour charger le fichier .pkl
    )
    
    # 3. CONFIGURATION DE L'INTELLIGENCE (Le modèle de discussion)
    llm = ChatMistralAI(model="mistral-medium")

    # 4. CRÉATION DE LA CHAÎNE RAG (Le lien entre tes données et l'IA)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff", # "stuff" veut dire qu'on donne les documents à l'IA
        retriever=vector_db.as_retriever(search_kwargs={"k": 3}) # On cherche les 3 meilleurs résultats
    )

    print("\n Chatbot prêt ! Pose-moi tes questions sur les événements à Paris.")
    print("(Tape 'quitter' pour fermer le programme)\n")
    
    # BOUCLE DE DISCUSSION
    while True:
        question = input(" Toi : ")
        
        if question.lower() == 'quitter':
            print(" Au revoir !")
            break
        
        print(" Recherche dans les fichiers...")
        # L'IA cherche dans FAISS, récupère le texte dans PKL et répond
        reponse = qa_chain.invoke(question)
        
        print(f"\n Chatbot : {reponse['result']}\n")
        print("-" * 50)

if __name__ == "__main__":
    lancer_chatbot()