# importing module
import os
import logging
from app.config import LOGPATH,LOGFILE,MODE

# Existence of log directory validation method
def validate_log_dir(logdir):
    if not os.path.isdir(logdir):
        os.makedirs(logdir)
    return True


def logger():

    _logdir = str(LOGPATH)

    # Method call to validate log directory
    if validate_log_dir(_logdir):
        # variable declaration
        log_file = os.path.join(_logdir, LOGFILE)

        # Create and configure logger
        logging.basicConfig(filename=log_file, format='%(asctime)s %(message)s', filemode='a')

        # Creating an object
        log_obj = logging.getLogger()

        # read config.ini for logmode and convert to upper for validating type of mode requested
        # based on the mode request, the loglevel to be setup

        mode = MODE.upper()

        if mode == "INFO":
            log_obj.setLevel(logging.INFO)
        elif mode == "DEBUG":
            log_obj.setLevel(logging.DEBUG)

        return log_obj