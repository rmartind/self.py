from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='selfbot',
    version='0.2.0',
    description='User bot for use with Discord API',
    long_description=readme,
    author='turingcmp',
    author_email='none',
    url='https://github.com/turingcmp/self.py.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
