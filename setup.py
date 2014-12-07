from setuptools import setup
import csvtools


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(name='csvtools',
      version=csvtools.__version__,
      description='A tiny library for handling CSV files.',
      long_description=read('README.rst'),
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

