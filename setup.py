try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
config = {
    'description': 'Control Dashboard. It aims to create a dashboard from which 
     you can restart services and ultimately see their status',
    'author': 'Jose M Mucientes',
    'url': 'https://github.com/jmuci/control-dashboard',
    'download_url': 'https://github.com/jmuci/control-dashboard',
    'author_email': 'jm.mucientes.fayos@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'control-dashboard'
}

