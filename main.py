import random

knowledge_base = {
    'Rule1': {'condition': 'app_type == "web"', 'language': ["Python", "JavaScript", "Java", "Ruby", "PHP", "Go"]},
    'Rule2': {'condition': 'app_type == "mobile"', 'language': ["Java", "Kotlin", "Swift", "Objective-C", "Flutter", "React Native"]},
    'Rule4': {'condition': 'app_type == "text" and performance', 'language': ["Bash/Shell", "Go"]},
    'Rule3': {'condition': 'app_type == "text" and not performance', 'language': ["Bash/Shell", "Python", "Perl", "Lua", "Go"]},
}

def infer(app_conditions):
    for rule, data in knowledge_base.items():
        condition = data['condition']
        language = data['language']

        if eval(condition, globals(), app_conditions):
            return language[random.randint(0, len(language)-1)]
    return None

def get_user_input():
    app_type = input("Podaj typ aplikacji: ").strip().lower()
    performance = input("Wydajnosc (y/n): ").strip().lower()
    if performance == "y":
        performance = True
    else:
        performance = False
    return {'app_type': app_type, "performance": performance}

if __name__ == "__main__":
    user_input = get_user_input()
    decision = infer(user_input)
    print("Decyzja: {}".format(decision))
