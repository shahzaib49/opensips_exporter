from setuptools import setup, find_packages

setup(
    name='opensips_exporter',
    version='0.1.0',
    description='Prometheus exporter using OpenSIPS MI commands with the help of native opensips-cli python module',
    author='Shahzaib Rana',
    author_email='shahzaibishtiaq94@gmail.com',
    packages=find_packages(),
    install_requires=[
        'prometheus_client',
        'opensipscli',  # if available via pip or include your local version
        # add any other dependencies
    ],
    entry_points={
        'console_scripts': [
            'opensips_exporter=opensips_exporter.main:main',
        ],
    },
)
