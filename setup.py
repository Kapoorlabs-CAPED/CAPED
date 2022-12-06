from setuptools import find_packages, setup
from os import path

_dir = path.dirname(__file__)


with open('README.md') as f:
    long_description = f.read()
with open(path.join(_dir,'caped_ai','_version.py'), encoding="utf-8") as f:
    exec(f.read())

setup(
    name="caped-ai",

    version=__version__,

    author='Varun Kapoor',
    author_email='varun.kapoor@kapoorlabs.org',
    url='https://github.com/Kapoorlabs-CAPED/CAPED-AI/',
    description='Content aware prediction and detection based on artificial intelligence.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        "oneat",
        "hydra-core",
        "viz-oneat",
        "caped-ai-metrics",
        "caped-ai-augmentations",
        "napatrackmater",
       
    ],
    packages = find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
    ],
)
