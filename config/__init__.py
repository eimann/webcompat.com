#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''This module handles application configuration and secrets.'''

from collections import namedtuple

from environment import *
from secrets import *

THREADS_PER_PAGE = 8

# ~3 months-ish expires for static junk
SEND_FILE_MAX_AGE_DEFAULT = 9000000

# Flask Limiter settings
# See http://flask-limiter.readthedocs.org/en/latest/#configuration
RATELIMIT_STORAGE_URL = 'memory://'
RATELIMIT_STRATEGY = 'moving-window'

DEBUG = False

if not PRODUCTION:
    DEBUG = True

# localhost runs on HTTP, use secure flag on session cookie otherwise.
if not LOCALHOST:
    SESSION_COOKIE_SECURE = True

# By default, we want to log CSP violations. See /csp-report in views.py.
CSP_LOG = True

# Logging Capabilities
# To benefit from the logging, you may want to add:
#   app.logger.info(Thing_To_Log)
# it will create a line with the following format
# 2015-09-14 20:50:19,185 INFO: Thing_To_Log [in /codepath/views.py:127]

LOG_FILE = '/tmp/webcompat.log'
LOG_FMT = '%(asctime)s tracking %(message)s'
CSP_REPORTS_LOG = '/tmp/webcompat-csp-reports.log'

# Status categories used in the project
# 'new', 'needsdiagnosis', 'needscontact', 'contactready' , 'sitewait', 'close'
# Creating the model
Category = namedtuple('Category', ['name', 'dataAttribute', 'label'])
CATEGORIES = []
cat_labels = [('needstriage', 'needstriage', 'Needs Triage'),
              ('needsDiagnosis', 'needsdiagnosis', 'Needs Diagnosis'),
              ('needsContact', 'needscontact', 'Needs Contact'),
              ('ready', 'contactready', 'Ready for Outreach'),
              ('sitewait', 'sitewait', 'Site Contacted'),
              ('close', 'closed', 'Closed')]
# populating the categories for issues status
for cat_label in cat_labels:
    CATEGORIES.append(Category(name=cat_label[0],
                               dataAttribute=cat_label[1],
                               label=cat_label[2]))

# labels that we allow to be added via a `label` GET param, when
# creating an issue.
EXTRA_LABELS = [
    'type-media',
    'type-webvr',
]
