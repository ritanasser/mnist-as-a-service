# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
import register as register
import upload as upload
from setuptools import setup, find_packages
import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig

setup_args = dict(
    name='fantastic_ascii',
    version='1.0.0',
    description='Fantastic ASCII',
    license='MIT',
    packages=find_packages(),
    author='Matt',
    author_email='example@example.com'
)
class register(register_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

class upload(upload_orig):

    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')

setup(
    name='myproj',

    cmdclass={
        'register': register,
        'upload': upload,
    }
)
if __name__ == '__main__':
    setup(**setup_args)