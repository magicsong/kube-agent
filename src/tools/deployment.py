from kubernetes import client, config

def load_k8s_config():
    config.load_kube_config()

def create_deployment_object(name, namespace, image, replicas):
    container = client.V1Container(name=name, image=image)
    template = client.V1PodTemplateSpec(metadata=client.V1ObjectMeta(labels={"app": name}),
                                         spec=client.V1PodSpec(containers=[container]))
    spec = client.V1DeploymentSpec(replicas=replicas, template=template)
    deployment = client.V1Deployment(api_version="apps/v1", kind="Deployment",
                                      metadata=client.V1ObjectMeta(name=name, namespace=namespace),
                                      spec=spec)
    return deployment

def deploy_application(deployment):
    api_instance = client.AppsV1Api()
    api_instance.create_namespaced_deployment(namespace=deployment.metadata.namespace,
                                               body=deployment)

def delete_deployment(name, namespace):
    api_instance = client.AppsV1Api()
    api_instance.delete_namespaced_deployment(name=name, namespace=namespace,
                                               body=client.V1DeleteOptions())