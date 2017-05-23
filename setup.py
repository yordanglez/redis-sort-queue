#!/usr/bin/env python
from setuptools import setup, find_packages
from redis_sort_queue import VERSION


setup(
    name='redis-sort-queue',
    version=VERSION,
    url='https://github.com/yordanglez/redis-sort-queue',
    description=(
        "ordered queue for redis"),
    long_description=open('README.rst').read(),
    author = "Yordano Gonzalez Fernandez",
    author_email = "yorda891216@gmail.com",
    keywords="Redis, Queue, Priority, Sort",
    platforms=['linux'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'redis'],

)