try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='statemachine',
      version='0.1',
      description='Simple Finite-State Machines',
      author='Kyle Conroy',
      author_email='kyle@kyleconroy.com',
      url='https://github.com/kyleconroy/statemachine',
      py_modules=['statemachine'],
     )
