import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(name='vantiv',
      version='0.0.6',
      description='vantiv SDK with samples',
      long_description=read('README.md'),
      license='MIT',
      classifiers=[
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.3',
                    'Programming Language :: Python :: 3.4',
                    'Programming Language :: Python :: 3.5',
                   ],
      author='Aleksander Sukharev',
      author_email='alexander.sukharev1@gmail.com',
      url='https://github.com/SambaDemon/python_vantiv.git',
      download_url='https://github.com/SambaDemon/python_vantiv/releases/tag/0.0.6',
      keywords='vantiv',
      include_package_data=True,
      packages=find_packages(),
      zip_safe=False, requires=['marshmallow', 'simplejson'])
