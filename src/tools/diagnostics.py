def analyze_application_health(k8s_client, app_name):
    """
    Analyze the health of a Kubernetes application.

    :param k8s_client: An instance of the Kubernetes client.
    :param app_name: The name of the application to analyze.
    :return: A report on the application's health status.
    """
    # Fetch the application deployment
    deployment = k8s_client.get_deployment(app_name)
    if not deployment:
        return f"Application '{app_name}' not found."

    # Check the status of the deployment
    replicas = deployment.status.replicas
    available_replicas = deployment.status.available_replicas
    if replicas == available_replicas:
        health_status = "Healthy"
    else:
        health_status = "Unhealthy"

    # Generate a report
    report = {
        "application": app_name,
        "replicas": replicas,
        "available_replicas": available_replicas,
        "health_status": health_status
    }

    return report


def report_application_status(report):
    """
    Report the status of a Kubernetes application.

    :param report: The report generated by the analyze_application_health function.
    """
    print(f"Application: {report['application']}")
    print(f"Replicas: {report['replicas']}")
    print(f"Available Replicas: {report['available_replicas']}")
    print(f"Health Status: {report['health_status']}")


def main():
    # Example usage
    from core.k8s_client import K8sClient

    k8s_client = K8sClient()
    app_name = "example-app"  # Replace with the actual application name
    report = analyze_application_health(k8s_client, app_name)
    report_application_status(report)


if __name__ == "__main__":
    main()