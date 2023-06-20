from setuptools import setup, find_packages


setup(
    name='clean_folder',
    version='1.0',
    description='Code small program',
    url='https://github.com/EfimenkoAlexey/homework_06/tree/main/clean_folder',
    author='Alexey Efimenko',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)