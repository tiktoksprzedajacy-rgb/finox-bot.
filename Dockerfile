# Używamy lekkiego Pythona
FROM python:3.11-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki projektu
COPY . .

# Instalujemy zależności
RUN pip install --no-cache-dir -r requirements.txt

# Uruchamiamy bota
CMD ["python3", "main.py"]
