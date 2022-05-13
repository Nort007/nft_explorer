import logging

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
# class CustomFormatter(logging.Formatter):
#     def __init__(self):
#         super().__init__()
#         self.grey = "\x1b[38;20m"
#         self.yellow = "\x1b[33;20m"
#         self.red = "\x1b[31;20m"
#         self.bold_red = "\x1b[31;1m"
#         self.reset = "\x1b[0m"
#         self.format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
#         self.FORMATS = {
#             logging.DEBUG: self.grey + self.format + self.reset,
#             logging.INFO: self.grey + self.format + self.reset,
#             logging.WARNING: self.yellow + self.format + self.reset,
#             logging.ERROR: self.red + self.format + self.reset,
#             logging.CRITICAL: self.bold_red + self.format + self.reset
#         }
#
#
#     def format(self, record):
#         log_fmt = self.FORMATS.get(record.levelno)
#         formatter = logging.Formatter(log_fmt)
#         return formatter.format(record)


logger = logging.getLogger("My_app")
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

ch.setFormatter(CustomFormatter())

logger.addHandler(ch)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")