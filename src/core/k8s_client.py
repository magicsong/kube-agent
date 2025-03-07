class K8sClient:
    def __init__(self, config):
        self.config = config
        self.api_client = self._initialize_api_client()

    def _initialize_api_client(self):
        # Initialize the Kubernetes API client using the provided config
        from kubernetes import client, config
        config.load_kube_config(self.config['kubeconfig'])
        return client.CoreV1Api()

    def get_pods(self, namespace):
        # Retrieve a list of pods in the specified namespace
        return self.api_client.list_namespaced_pod(namespace)

    def create_deployment(self, namespace, deployment_manifest):
        # Create a deployment in the specified namespace
        from kubernetes import client
        deployment = client.V1Deployment(**deployment_manifest)
        return self.api_client.create_namespaced_deployment(namespace, deployment)

    def delete_deployment(self, namespace, deployment_name):
        # Delete a deployment in the specified namespace
        return self.api_client.delete_namespaced_deployment(deployment_name, namespace)

    def get_services(self, namespace):
        # Retrieve a list of services in the specified namespace
        return self.api_client.list_namespaced_service(namespace)

    def create_service(self, namespace, service_manifest):
        # Create a service in the specified namespace
        from kubernetes import client
        service = client.V1Service(**service_manifest)
        return self.api_client.create_namespaced_service(namespace, service)

    def delete_service(self, namespace, service_name):
        # Delete a service in the specified namespace
        return self.api_client.delete_namespaced_service(service_name, namespace)