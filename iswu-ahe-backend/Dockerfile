# Użyj oficjalnego obrazu Pythona jako bazowego obrazu
FROM python:3.10

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Skopiuj plik wymagań i instaluj zależności
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Skopiuj resztę aplikacji do katalogu roboczego w kontenerze
COPY . .

# Uruchom aplikację
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
