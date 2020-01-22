import logging
import time


logger_name = 'logger'
filename = 'sample.log'
datefmt = '%d-%m %H:%M:%S'

logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(filename)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt)
fh.setFormatter(formatter)
logger.addHandler(fh)


logger.debug('This is debug message')
logger.info('Informational message')
logger.error('An error has happened!')
