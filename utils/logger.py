import logging,sys
from tqdm import tqdm
import io

__all__ = ['initialise_logger']

def initialise_logger(logname = sys.modules['__main__'].__name__, verbose = False ,logfile = '/dev/null',stream = True):
    """
    Setting up the main logger

    :param options:
    :return:
    """
    # define base logger
    logger = logging.getLogger(logname)
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    # define file handler and stream handler
    fh = logging.FileHandler(logfile)
    fh.setLevel(logging.DEBUG if verbose else logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(level= logging.INFO)
    # define format
    formatter_fh = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s : \t %(message)s')
    formatter_ch = logging.Formatter('%(levelname)s:%(name)s: %(message)s')
    fh.setFormatter(formatter_fh)
    ch.setFormatter(formatter_ch)
    # add the handlers to the logger
    logger.addHandler(fh)
    if stream : logger.addHandler(ch)
    return


class TqdmToLogger(io.StringIO):
    """
        Output stream for TQDM which will output to logger module instead of
        the StdOut.
    """
    logger = None
    level = None
    buf = ''
    def __init__(self,logger,level=None):
        super(TqdmToLogger, self).__init__()
        self.logger = logger
        self.level = level or logging.INFO
    def write(self,buf):
        self.buf = buf.strip('\r\n\t ')
    def flush(self):
        self.logger.log(self.level, self.buf)

