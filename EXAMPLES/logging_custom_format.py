import logging

class ColumnFormat(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%', validate=True, *, defaults=None):
        self.fmt = fmt
        self.datefmt = datefmt
        self.style = style
        self.validate = validate˙
        self.defaults = defaults

    def format(self, record):
        # if self.fmt is None:
        # print(f"{dir(record) = }")
        return f"{record.levelname:10} {record.name:10} {record.msg}"

column_formatter = ColumnFormat(None, None, '%', )

handler = logging.FileHandler(filename="custom.log")
handler.setFormatter(column_formatter)

logger = logging.getLogger("EXPERIMENT")
logger.addHandler(handler)

logger.error("message 1")
logger.debug("debugging message")
logger.warning("this is a warning")
logger.critical("Oh no!!")
