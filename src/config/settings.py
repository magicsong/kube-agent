DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'k8s_db'
}

K8S_CONFIG = {
    'kubeconfig_path': '/path/to/your/kubeconfig',
    'namespace': 'default',
    'context': 'your_context'
}

LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(message)s'
        }
    }
}