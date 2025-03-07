import unittest
from src.agents.yaml_editor_agent import YamlEditorAgent

class TestYamlEditorAgent(unittest.TestCase):

    def setUp(self):
        self.agent = YamlEditorAgent()

    def test_load_yaml(self):
        yaml_content = self.agent.load_yaml('k8s_examples/deployment.yaml')
        self.assertIsNotNone(yaml_content)
        self.assertIn('apiVersion', yaml_content)
        self.assertIn('kind', yaml_content)

    def test_edit_yaml(self):
        yaml_content = self.agent.load_yaml('k8s_examples/deployment.yaml')
        modified_content = self.agent.edit_yaml(yaml_content, {'spec': {'replicas': 3}})
        self.assertEqual(modified_content['spec']['replicas'], 3)

    def test_validate_yaml(self):
        valid_yaml = self.agent.load_yaml('k8s_examples/deployment.yaml')
        self.assertTrue(self.agent.validate_yaml(valid_yaml))

        invalid_yaml = "invalid: yaml: content"
        self.assertFalse(self.agent.validate_yaml(invalid_yaml))

if __name__ == '__main__':
    unittest.main()