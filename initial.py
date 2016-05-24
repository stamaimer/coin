
import sys

from coin.logger import init_logger

init_logger()

from coin.utils import create_database, resets_database, create_user

create_database(sys.argv[1])

create_user(sys.argv[1])

resets_database()
