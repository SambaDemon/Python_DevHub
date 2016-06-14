import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
        README = f.read()

setup(name='vantiv',
      version='0.0.3',
      description='vantiv SDK with samples',
      long_description=README + '\n\n',
      classifiers=[
                    "Framework :: Any",
                    "Programming Language :: Python :: 3.5",
                    ],
      author='Aleksander Sukharev',
      author_email='alexander.sukharev1@gmail.com',
      url='https://github.com/SambaDemon/python_vantiv.git',
      download_url='https://github.com/SambaDemon/python_vantiv/releases/tag/0.0.3',
      keywords='vantiv',
      include_package_data=True,
      packages=find_packages(),
      zip_safe=False, requires=['marshmallow', 'simplejson'])
