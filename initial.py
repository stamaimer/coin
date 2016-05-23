
from coin.logger import init_logger

init_logger()

from coin.utils.create_db import create_db

create_db()

from coin.models import init_db

init_db()