from setuptools import find_packages, setup


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mylogging',
    version='0.0.4',
    description='logging package for myself',
    long_description=readme,
    license=license,
    author='Shun Fukusumi',
    author_email='shun.fukusumi@gmail.com',
    url='https://github.com/juv-shun/mylogging',
    packages=find_packages(exclude=('tests')),
    test_suite='tests',
)
