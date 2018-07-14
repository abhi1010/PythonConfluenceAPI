from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

try:
    from future import standard_library
    standard_library.install_aliases()
except:
    pass

__author__ = 'Robert Cope, Pushrod Technology'

from .api import ConfluenceAPI, all_of
from .cfapi import ConfluenceFuturesAPI
