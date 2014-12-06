from setuptools import setup
import csvtools


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='csvtools',
      version=csvtools.__version__,
      description='A tiny library for handling CSV files.',
      long_description=readme(),
      classifiers=[
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
          ],
      author='Taurus Olson',
      author_email=u'taurusolson@gmail.com',
      url='https://github.com/TaurusOlson/csvtools',
      packages=['csvtools'],
      keywords='csv tools',
      license=csvtools.__license__,
      include_package_data=True,
      zip_safe=False
      )

