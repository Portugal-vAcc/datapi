#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Portugal-vAcc Data API
Copyright (C) 2018  Pedro Rodrigues <prodrigues1990@gmail.com>

This file is part of Portugal-vAcc Data API.

Portugal-vAcc is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

Portugal-vAcc Data API is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Portugal-vAcc Data API. If not, see <http://www.gnu.org/licenses/>.
"""
import os

MONGO_URI = os.environ.get('MONGO_URI',
                           'mongodb://localhost:27017/vaccdatapi')

NEWS_ENDPOINT = {
    'schema': {
        'title': {
            'type': 'string',
            'required': True,
        },
        'content': {
            'type': 'string',
            'required': True,
        },
    },
    'resource_methods': ['GET', 'POST'],
}
DOMAIN = {'news': NEWS_ENDPOINT}
