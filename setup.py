from setuptools import setup, find_packages

setup(
    name='k8s-langraph-tool',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool for Kubernetes operations including diagnostics, deployment, and YAML editing.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'kubernetes>=12.0.0',
        'pyyaml>=5.4.1',
        'click>=8.0.0'
    ],
    entry_points={
        'console_scripts': [
            'k8s-langraph=k8s-langraph-tool.ui.cli:main',
        ],
    },
)