import streamlit as st
import pandas as pd
import requests
import os 

st.set_page_config(page_title="Kubernetes Frontend")

st.title("🖥 Kubernetes Frontend")
st.write("Bienvenue sur l'application frontend déployée sur Kubernetes !")
st.write("Cette application interagit avec le backend API pour récupérer des données depuis la base MySQL.")

if os.environ.get("env") == "production":
    API_BASE = "http://api-service.mplatteau.svc.cluster.local:8000"
else:
    API_BASE = "http://4.251.145.205"

st.markdown("---")

# Section 1: Fetch all clients
st.header("📋 Tous les clients")
if st.button("Récupérer tous les clients"):
    try:
        print(API_BASE)
        response = requests.get(f"{API_BASE}/clients")
        if response.status_code == 200:
            data = response.json()
            if data:
                df = pd.DataFrame(data)
                st.dataframe(df)
            else:
                st.warning("Aucun client trouvé.")
        else:
            st.error(f"Erreur {response.status_code} lors de la récupération des clients.")
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")

st.markdown("---")

# Section 2: Search client by ID
st.header("🔍 Rechercher un client par ID")
client_id = st.text_input("Entrez l'ID du client")

if st.button("Rechercher"):
    if client_id.strip() == "":
        st.warning("Veuillez entrer un ID de client.")
    else:
        try:
            response = requests.get(f"{API_BASE}/clients/{client_id}")
            if response.status_code == 200:
                client_data = response.json()
                if client_data:
                    df = pd.DataFrame([client_data])
                    st.dataframe(df)
                else:
                    st.info(f"Aucun client trouvé avec l'ID {client_id}.")
            elif response.status_code == 404:
                st.info(f"Aucun client trouvé avec l'ID {client_id}.")
            else:
                st.error(f"Erreur {response.status_code} lors de la récupération du client.")
        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")


