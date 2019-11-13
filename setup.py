from setuptools import setup
import setuptools
setup(
    name='tan_egg',
    version='1.0.0',
    packages=['math', 'unittest'],
    url='',
    license='',
    entrypoints = ['setuptools.installation','proj.tan_func:tan_fun'],
    author='novin.patrick',
    author_email='',
    description=''
)
