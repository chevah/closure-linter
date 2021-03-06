#!/usr/bin/env python
#
# Copyright 2010 The Closure Linter Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup


setup(name='chevah-js-linter',
      version='2.4.0',
      description='Chevah JS Linter',
      license='Apache',
      author='The Closure Linter Authors',
      author_email='adiroiban@gmail.com',
      url='https://github.com/chevah/chevah-js-linter',
      install_requires=['python-gflags', 'six'],
      tests_require=['mox'],
      package_dir={'closure_linter': 'closure_linter'},
      packages=['closure_linter', 'closure_linter.common'],
      entry_points = {
        'console_scripts': [
          'gjslint = closure_linter.gjslint:main',
          'fixjsstyle = closure_linter.fixjsstyle:main'
        ]
      },
      test_suite='closure_linter.testutil.run_all',
)
