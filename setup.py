from importlib.metadata import entry_points
from setuptools import setup

setup(
    name='specialfolderpath',
    version='1.0',
    description='Get the path of a special folder',
    entry_points={
        'console_scripts': [
            'special_folder_path = specialfolderpath.special_folder_path:main',
        ]
    }
)

