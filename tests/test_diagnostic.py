import unittest
from src.agents.diagnostic_agent import DiagnosticAgent

class TestDiagnosticAgent(unittest.TestCase):

    def setUp(self):
        self.agent = DiagnosticAgent()

    def test_health_check(self):
        result = self.agent.health_check()
        self.assertIsInstance(result, dict)
        self.assertIn('status', result)
        self.assertIn('details', result)

    def test_analyze_application(self):
        app_name = "test-app"
        result = self.agent.analyze_application(app_name)
        self.assertIsInstance(result, dict)
        self.assertIn('app_name', result)
        self.assertIn('issues', result)

    def test_get_diagnostics_report(self):
        report = self.agent.get_diagnostics_report()
        self.assertIsInstance(report, str)
        self.assertGreater(len(report), 0)

if __name__ == '__main__':
    unittest.main()