import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(levelname)s - %(message)s')
fh = logging.FileHandler('employee.log')
fh.setFormatter(fmt)
logger.addHandler(fh)

logger.info("Hello")

