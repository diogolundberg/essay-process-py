import logging
import logging.handlers
from os import getcwd, path

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

LOG_FILE = path.join(getcwd(), 'requests.log')
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
