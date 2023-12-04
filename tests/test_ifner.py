import unittest

import app.inference as ai

knowledge_base = [
    ('app_type == "web" and not performance', ["Python", "JavaScript", "Java", "Ruby", "PHP", "Go"]),
    ('app_type == "web" and performance', ["JavaScript", "Java", "Go"]),
    ('app_type == "mobile" and performance', ["Java", "Kotlin", "Swift"]),
    ('app_type == "mobile" and not performance', ["Java", "Kotlin", "Swift", "Objective-C", "Flutter", "React-Native"]),
    ('app_type == "text"', ["Bash/Shell", "Go"]),
    ('app_type == "text" and not performance', ["Bash/Shell", "Python", "Perl", "Lua", "Go"])
]


class TestInferenceSystem(unittest.TestCase):

    def test_web_application_with_performance(self):
        user_input = {'app_type': 'web', 'performance': True}
        decision = ai.infer(user_input, knowledge_base)
        self.assertIn(member=decision, container=["Python", "JavaScript", "Java", "Ruby", "PHP", "Go"])

    def test_web_application_without_performance(self):
        user_input = {'app_type': 'web', 'performance': False}
        decision = ai.infer(user_input, knowledge_base)
        self.assertIn(member=decision, container=["Python", "JavaScript", "Java", "Ruby", "PHP", "Go"])

    def test_mobile_application_with_performance(self):
        user_input = {'app_type': 'mobile', 'performance': True}
        decision = ai.infer(user_input, knowledge_base)
        self.assertIn(member=decision, container=["Java", "Kotlin", "Swift"])

    def test_mobile_application_without_performance(self):
        user_input = {'app_type': 'mobile', 'performance': False}
        decision = ai.infer(user_input, knowledge_base)
        self.assertIn(member=decision, container=["Java", "Kotlin", "Swift", "Objective-C", "Flutter", "React-Native"])

    def test_text_application_with_performance(self):
        user_input = {'app_type': 'text', 'performance': True}
        decision = ai.infer(user_input, knowledge_base)
        self.assertIn(member=decision, container=["Bash/Shell", "Go"])

    def test_text_application_without_performance(self):
        user_input = {'app_type': 'text', 'performance': False}
        decision = ai.infer(user_input, knowledge_base)
        self.assertIn(member=decision, container=["Bash/Shell", "Python", "Perl", "Lua", "Go"])

    def test_unknown_application(self):
        user_input = {'app_type': 'unknown', 'performance': True}
        decision = ai.infer(user_input, knowledge_base)
        self.assertEqual(first=decision, second=None)


if __name__ == '__main__':
    unittest.main()
