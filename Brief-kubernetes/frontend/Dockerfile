# 1️⃣ Choix de l'image Python
FROM python:3.12-slim

# 2️⃣ Définir le répertoire de travail
WORKDIR /app

# 3️⃣ Copier les fichiers de projet
COPY pyproject.toml ./
COPY uv.lock ./
COPY . .

# 4️⃣ Installer uv et les dépendances du projet
RUN pip install --upgrade pip \
    && pip install uv \
    && uv sync

# 5️⃣ Exposer le port Streamlit
EXPOSE 8501

# 6️⃣ Commande pour lancer Streamlit
CMD ["uv", "run", "streamlit", "run", "frontend.py", "--server.port=8501", "--server.headless=true"]
