import logging

import coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', fmt='%(asctime)s: %(levelname)s: [%(funcName)s: %(filename)s: %(module)s:] %(message)s')
