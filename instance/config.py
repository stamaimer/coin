SECRET_KEY="stamaimer"

DB="mysql"

DB_DRIVER="pymysql"

DB_USER="stamaimer"
DB_PSWD="123456"
DB_HOST="192.168.0.104"
DB_NAME="coin"

SQLALCHEMY_DATABASE_URI="%s+%s://%s:%s@%s/%s" % (DB,
                                                 DB_DRIVER,
                                                 DB_USER,
                                                 DB_PSWD,
                                                 DB_HOST,
                                                 DB_NAME)
