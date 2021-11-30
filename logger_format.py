try:
    import logging
    import os
    from datetime import date
    from pythonjsonlogger import jsonlogger
except ImportError as err:
    print(f"ImportError; {err}")
    exit(1)


def log_path_checker(logfile_name):
    """
    Check log path existance if not create one
    :param logfile_name: file name as log file name created 
    :return: filepath
    """
    logPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Logs')
    if not os.path.exists(logPath):
        os.mkdir(logPath)
    pathname, file_name = os.path.split(logfile_name)
    logfile = os.path.join(logPath, str(date.today().strftime('%d_%m_%Y')) + '_' + file_name.split('.')[0] + '.log')
    return logfile


def setup_logging(logfile_name):
    """
    set common logging json format using pythonjsonlogger.
    This structured way of json format is designed to make kibana dashboard
	:param logfile: file name as log file name created 
    :return: json format logger class which includes level, jsonhandler, message,levelname,etc
    """
    logfile = log_path_checker(logfile_name)
    if os.path.exists(logfile):
        json_handler = logging.FileHandler(logfile, mode='a')
    else:
        json_handler = logging.FileHandler(logfile, mode='w')
    format_str = '%(levelname)%(asctime)%(message)%(exc_info)'
    formatter = jsonlogger.JsonFormatter(format_str)
    json_handler.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(json_handler)
    logger.setLevel('INFO')
    return logger
