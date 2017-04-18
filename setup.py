from setuptools import setup, find_packages

setup(
    name = 'piecewise_distortion',
    version = '0.1',
    description = 'A package to manage image distortion',
    license = 'MIT',
    author = 'sukohi',
    author_email = 'sukohi.capilano@gmail.com',
    url = 'https://github.com/SUKOHI',
    keywords = 'distort image',
    packages = find_packages(),
    install_requires = ['numpy', 'scikit-image', 'pillow'],)
