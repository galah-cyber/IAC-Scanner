from setuptools import setup, find_packages

setup(
   name='IACScanner',
   version='1.0',
   author='Galah Cyber',
   packages=find_packages(),
   license='MIT',
   entry_points={"console_scripts": ["IACScanner = IACScanner.main:run"]}
)