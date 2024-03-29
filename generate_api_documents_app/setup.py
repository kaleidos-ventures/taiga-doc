#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos INC


from setuptools import setup

setup(
    name='generate-api-documents',
    version="0.0.1",
    description="Helper app to generate requests and responses from taiga API",
    long_description="",
    keywords='taiga, documentation, api',
    author='Jesús Espino García',
    author_email='jesus.espino@kaleidos.net',
    url='https://github.com/taigaio/taiga-doc',
    license = 'MPL-2',
    packages=[
        "generate_api_documents"
    ],
    package_data={
        "generate_api_documents": [
            "management/commands/*.json",
            "management/commands/*.py",
            "management/commands/*.png",
        ]
    },
    install_requires=[
        'django >= 1.7',
    ],
    classifiers=[
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
