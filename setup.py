try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Airtable API, but in Python',
    'author': 'John Louie',
    'url': 'URL',
    'download_url': 'DOWNLOAD_URL',
    'author_email': 'jlouie95618@gmail.com',
    'version': '0.1',
    'install_requires': ['nose', 'requests[security]'], # does including the [security] work?
    'packages': ['airtable'],
    'scripts': [],
    'name': 'Airtable'
}

setup(**config)
