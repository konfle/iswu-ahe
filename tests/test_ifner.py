import unittest

from iswu.main import infer

class TestInferenceSystem(unittest.TestCase):

    def test_web_application(self):
        user_input = {'app_type': 'web', 'performance': True}
        decision = infer(user_input)
        self.assertIn(decision, ["Python", "JavaScript", "Java", "Ruby", "PHP", "Go"])

    def test_mobile_application(self):
        user_input = {'app_type': 'mobile', 'performance': True}
        decision = infer(user_input)
        self.assertIn(decision, ["Java", "Kotlin", "Swift", "Objective-C", "Flutter", "React Native"])

    def test_text_application_with_performance(self):
        user_input = {'app_type': 'text', 'performance': True}
        decision = infer(user_input)
        self.assertIn(decision, ["Bash/Shell", "Go"])

    def test_text_application_without_performance(self):
        user_input = {'app_type': 'text', 'performance': False}
        decision = infer(user_input)
        self.assertIn(decision, ["Bash/Shell", "Python", "Perl", "Lua", "Go"])

    def test_unknown_application(self):
        user_input = {'app_type': 'unknown', 'performance': True}
        decision = infer(user_input)
        self.assertIsNone(decision)

if __name__ == '__main__':
    unittest.main()
