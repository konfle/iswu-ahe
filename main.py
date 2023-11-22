import random

# Wiedza ekspertów na temat języków programowania w zależności od warunków aplikacji
knowledge_base = {
    'Rule1': {'condition': 'app_type == "web"', 'language': ["Python", "JavaScript", "Java", "Ruby", "PHP", "Go"]},
    'Rule2': {'condition': 'app_type == "mobile" and performance', 'language': ["Java", "Kotlin", "Swift"]},
    'Rule3': {'condition': 'app_type == "mobile" and not performance', 'language': ["Java", "Kotlin", "Swift", "Objective-C", "Flutter", "React Native"]},
    'Rule4': {'condition': 'app_type == "text"', 'language': ["Bash/Shell", "Go"]},
    'Rule5': {'condition': 'app_type == "text" and not performance', 'language': ["Bash/Shell", "Python", "Perl", "Lua", "Go"]},
}

# Funkcja wnioskująca język programowania w zależności od warunków aplikacji
def infer(app_conditions):
    for rule, data in knowledge_base.items():
        condition = data['condition']
        language = data['language']

        # Sprawdzenie, czy warunek reguły jest spełniony
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
    # Pobranie danych od użytkownika, podjęcie decyzji i wydrukowanie wyniku
    user_input = get_user_input()
    decision = infer(user_input)
    print("Decyzja: {}".format(decision))
