"""
Python 3 Gearman API - Client, worker, and admin client interfaces
"""

from python3_gearman.admin_client import GearmanAdminClient
from python3_gearman.client import GearmanClient
from python3_gearman.worker import GearmanWorker

from python3_gearman.connection_manager import DataEncoder
from python3_gearman.constants import PRIORITY_NONE, PRIORITY_LOW, \
    PRIORITY_HIGH, JOB_PENDING, JOB_CREATED, JOB_FAILED, JOB_COMPLETE

import logging

__version__ = '0.1.0'
name = 'python3_gearman'


class NullHandler(logging.Handler):

    def emit(self, record):
        pass

gearman_root_logger = logging.getLogger('python3_gearman')
gearman_root_logger.addHandler(NullHandler())
