import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name='Tacklets',
      version='0.5.0',
      description='Collection of plugins for Tackle, business oriented CMS',
      long_description = read('README.rst') + u"\n" + \
          read('TACKLETS.rst') +  u"\n" + \
          read('COMPAT.rst') +  u"\n" + \
          read('src/tacklets/project/doc/README.rst'),
      author='Ilshad Khabibullin',
      author_email='astoon@spacta.com',
      url='',
      test_suite='tacklets',
      license="BSD",
      zip_safe=False,
      include_package_data=True,
      packages=find_packages('src'),
      package_dir={'':'src'},
      install_requires=[]
      )
