import psycopg2
import os
from dotenv import load_dotenv

knowledge_base = [
    ('app_type == "web"', ["Python", "JavaScript", "Java", "Ruby", "PHP", "Go"]),
    ('app_type == "mobile" and performance', ["Java", "Kotlin", "Swift"]),
    ('app_type == "mobile" and not performance', ["Java", "Kotlin", "Swift", "Objective-C", "Flutter", "React-Native"]),
    ('app_type == "text"', ["Bash/Shell", "Go"]),
    ('app_type == "text" and not performance', ["Bash/Shell", "Python", "Perl", "Lua", "Go"])
]

# Wczytaj zmienne środowiskowe z pliku .env
load_dotenv()

# Uzyskaj wartości zmiennych środowiskowych
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Funkcja pobierająca wiedzę ekspercką z bazy danych
def get_rules_from_database(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    cursor = conn.cursor()
    cursor.execute('SELECT condition, languages FROM knowledge_base')
    rules = cursor.fetchall()
    conn.close()
    return rules
