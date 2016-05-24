
from coin.logger import init_logger

init_logger()

from coin.utils import create_db, init_db

create_db()

init_db()