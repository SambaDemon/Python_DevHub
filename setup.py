import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
        README = f.read()

requires = []

setup(name='vantiv',
      version='0.1.0',
      description='pyramid_ipauth',
      long_description=README + '\n\n',
      classifiers=[
                    "Programming Language :: Python",
                    "Framework :: Any",
                    "Programming Language :: Python",
                    "Programming Language :: Python :: 2.6",
                    "Programming Language :: Python :: 2.7",
                    "Programming Language :: Python :: 3.1",
                    "Programming Language :: Python :: 3.2",
                    "Programming Language :: Python :: 3.3",
                    "Programming Language :: Python :: 3.4",
                    "Programming Language :: Python :: 3.5",
                    ],
      author='Aleksander Sukharev',
      url='https://github.com/SambaDemon/Python_DevHub',
      keywords='vantiv',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires)
