from setuptools import setup
import csvlib


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='csvlib',
      version=csvlib.__version__,
      description='A tiny library for handling CSV files.',
      long_description=readme(),
      classifiers=[
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
          ],
      author='Taurus Olson',
      author_email=u'taurusolson@gmail.com',
      url='https://github.com/TaurusOlson/csvlib',
      packages=['csvlib'],
      keywords='csv tools',
      license=csvlib.__license__,
      include_package_data=True,
      zip_safe=False
      )

