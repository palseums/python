import logging
logging.basicConfig(filename='demo.log',filemode='w',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s ')
#logging.disable()
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("Error message")
logging.critical("Critical message")

#filemode default is append filemode='a'
# level=logging.Warning is the default one
# 10 - debug - logging.debug() - Lowest level
# 20 - info - logging.info() Record general information
# 30 - Warning - logging.warning() Potential issues which may cause errors in the future
# 40 - Error - logging.error() - Record errors which cause a section of the code to fail
# 50 - Critical logging.critical - Highest level of Blockers which fails your whole program

# https://docs.python.org/3/library/logging.html#logrecord-attributes


