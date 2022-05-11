# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
from setuptools import setup, find_packages
import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig
from setuptools import setup

setup_args = dict(
    name='fantastic_ascii',
    version='1.0.0',
    description='Fantastic ASCII',
    license='MIT',
    packages=find_packages(),
    author='Matt',
    author_email='example@example.com'
)

if __name__ == '__main__':
    setup(**setup_args)