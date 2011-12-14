from setuptools import setup, find_packages

setup(name='furl',
      version='0.2',
      packages=find_packages(),
      author='Arthur Grunseid',
      author_email='grunseid@gmail.com',
      url='https://github.com/gruns/furl',
      license='Unlicense',
      include_package_data=True,
      description='URL manipulation made simple.',
      long_description='URL parsing and manipulation made simple.',
      platforms=['any'],
      classifiers='',
      install_requires=[''],
      test_suite='tests',
      tests_require=[],
      )