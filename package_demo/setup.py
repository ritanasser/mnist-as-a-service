# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
from setuptools import setup, find_packages

setup_args = dict(
    name='fantastic_ascii',
    version='1.0.1',
    description='Fantastic ASCII',
    license='MIT',
    packages=find_packages(),
    author='Matt',
    author_email='example@example.com',
    insatall_requires=['PyYAML>3.11', 'twine', 'wheel'],
)

if __name__ == '__main__':
    setup(**setup_args)
