from distutils.core import setup
from setuptools import find_packages
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip


def list_dependencies(pipfile):
    return convert_deps_to_pip(pipfile['packages'], r=False)

def list_dev_dependencies(pipfile):
    return convert_deps_to_pip(pipfile['dev-packages'], r=False)


pipfile = Project(chdir=False).parsed_pipfile
setup(
    name='ping',
    author='TIOXY Org.',
    author_email='gabrieltiossi@gmail.com',
    packages=find_packages(),
    license='LICENSE',
    description='pong',
    long_description='pong',
    install_requires=list_dependencies(pipfile),
    extras_require={
        'dev': list_dev_dependencies(pipfile),
    }
)
