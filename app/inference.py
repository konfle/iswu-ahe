import random

# Funkcja wnioskująca język programowania w zależności od warunków aplikacji
def infer(app_conditions, rules):
    for condition, language in rules:
        if eval(condition, globals(), app_conditions):
            # Losowy wybór języka z dostępnych
            return language[random.randint(0, len(language)-1)]
    return None
