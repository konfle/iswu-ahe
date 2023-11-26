import random
import psycopg2
import os

from psycopg2 import sql
from dotenv import load_dotenv


# Wczytaj zmienne środowiskowe z pliku .env
load_dotenv()

# Uzyskaj wartości zmiennych środowiskowych
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Funkcja pobierająca wiedzę ekspercką z bazy danych
def get_rules_from_database():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    cursor.execute('SELECT condition, languages FROM knowledge_base')
    rules = cursor.fetchall()
    conn.close()
    return rules

# Funkcja wnioskująca język programowania w zależności od warunków aplikacji
def infer(app_conditions, rules):
    for condition, language in rules:
        if eval(condition, globals(), app_conditions):
            # Losowy wybór języka z dostępnych
            return language[random.randint(0, len(language)-1)]
    return "Coś poszło nie tak..."
    
# Funkcja pobierająca dane od użytkownika
def get_user_input():
    app_type = input("Podaj typ aplikacji: ").strip().lower()
    performance = input("Wydajnosc (y/n): ").strip().lower()
    if performance == "y":
        performance = True
    else:
        performance = False
    return {'app_type': app_type, "performance": performance}

if __name__ == "__main__":
    # Pobierz reguły wiedzy ekspertów z bazy danych PostgreSQL
    rules_from_db = get_rules_from_database()

    # Pobranie danych od użytkownika, podjęcie decyzji i wydrukowanie wyniku
    user_input = get_user_input()
    decision = infer(user_input, rules_from_db)
    print("Decyzja: {}".format(decision))
