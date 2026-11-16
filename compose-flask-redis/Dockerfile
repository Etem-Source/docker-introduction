# Image de base minimale et versionnée
FROM python:3.13-alpine

# Pas de fichiers .pyc, logs affichés directement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Utilisateur non-root
RUN addgroup -S -g 10001 appgroup \
    && adduser -S -u 10001 -G appgroup appuser

# Dépendances d'abord (meilleur cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code de l'application
COPY app.py .

USER 10001:10001
EXPOSE 5000

# Serveur de production gunicorn (2 workers)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]