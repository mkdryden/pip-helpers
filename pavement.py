import sys
import os

from paver.easy import task, needs
from paver.setuputils import setup

sys.path.insert(0, os.path.dirname(__file__))
import version


setup(name='pip_helpers',
      version=version.getVersion(),
      description='Helper functions for installing, etc. using `pip`',
      author='Christian Fobel',
      author_email='christian@fobel.net',
      url='http://github.com/wheeler-microfluidics/pip_helpers.git',
      license='GPLv2',
      install_requires=['natsort', 'pip>=6.0', 'requests'],
      packages=['pip_helpers'])


@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass
