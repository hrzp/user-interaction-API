from setuptools import setup

setup(
    name='app',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'connexion[swagger-ui]',
        'autopep8',
        'pylint'
    ],
)
