from setuptools import setup
from pip.req import parse_requirements

import sbctorrent

install_reqs = parse_requirements('requirements.txt', session='hack')
reqs = [str(el.req) for el in install_reqs]

setup(name=sbctorrent.__title__,
      version=sbctorrent.__version__,
      description=sbctorrent.__summary__,
      url=sbctorrent.__url__,
      author=sbctorrent.__author__,
      author_email=sbctorrent.__email__,
      license=sbctorrent.__license__,
      packages=['sbctorrent'],
      install_requires=reqs
      )
