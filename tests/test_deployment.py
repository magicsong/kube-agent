import unittest
from src.agents.deployment_agent import DeploymentAgent

class TestDeploymentAgent(unittest.TestCase):

    def setUp(self):
        self.agent = DeploymentAgent()

    def test_deploy_application(self):
        # Mock deployment parameters
        app_name = "test-app"
        namespace = "default"
        yaml_file = "k8s_examples/deployment.yaml"
        
        # Call the deployment method
        result = self.agent.deploy_application(app_name, namespace, yaml_file)
        
        # Assert the expected outcome
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], f"Application {app_name} deployed successfully.")

    def test_update_application(self):
        # Mock update parameters
        app_name = "test-app"
        namespace = "default"
        yaml_file = "k8s_examples/deployment.yaml"
        
        # Call the update method
        result = self.agent.update_application(app_name, namespace, yaml_file)
        
        # Assert the expected outcome
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], f"Application {app_name} updated successfully.")

    def test_delete_application(self):
        # Mock deletion parameters
        app_name = "test-app"
        namespace = "default"
        
        # Call the delete method
        result = self.agent.delete_application(app_name, namespace)
        
        # Assert the expected outcome
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], f"Application {app_name} deleted successfully.")

if __name__ == '__main__':
    unittest.main()