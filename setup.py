#!/usr/bin/env python
from distutils.core import setup


setup(
    name='redis-sort-queue',
    version='0.0.2',
    url='https://github.com/yordan.glez/redis-sort-queue',
    description=(
        "ordered queue for redis"),
    long_description=open('README.rst').read(),
    author = "Yordano Gonzalez Fernandez",
    author_email = "yorda891216@gmail.com",
    keywords="Redis, Queue, Priority, Sort",
    license=open('LICENSE').read(),
    platforms=['linux'],
    packages=['redis-sort-queue'],
    # include_package_data=True,
    install_requires=[
        'redis'],
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    # classifiers=[
    #     'Development Status :: 4 - Beta',
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: BSD License',
    #     'Operating System :: Unix',
    #     'Programming Language :: Python',
    #     'Programming Language :: Python :: 2',
    #     'Programming Language :: Python :: 2.7',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.3',
    #     'Programming Language :: Python :: 3.4',
    #     'Topic :: Other/Nonlisted Topic'],
)
