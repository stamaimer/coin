
from coin.logger import init_logger

init_logger()

from coin.utils import create_database, resets_database, create_user

create_database("123456")

create_user("123456")

resets_database()