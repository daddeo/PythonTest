# Mixins (aka multiple-inheritance)
# used to streamline repetative operations
#
# https://docs.python.org/3/tutorial/classes.html#multiple-inheritance
# https://docs.python.org/3/library/functions.html#super
#


class Loggable:
    def __init__(self):
        self.message = ""

    def log(self):
        print("Log message from " + self.message)


class Connection:
    def __init__(self):
        self.server = ""

    def connect(self):
        print("Connecting to database on " + self.server)


class SqlDatabase(Connection, Loggable):
    def __init__(self):
        super().__init__()
        self.message = "Sql Connection Demo"
        self.server = "MSSQLServer"


class Database(Connection):
    def __init__(self):
        super().__init__()
        self.server = "MySQL"


class ConsoleLogger(Loggable):
    def __init__(self):
        super().__init__()
        self.message = "Logger Demo"


def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Loggable):
        item.log()


sql_connection = SqlDatabase()
# Connecting to database on Some_Server
# Log message from Sql Connection Demo
framework(sql_connection)

db_connection = Database()
# Connecting to database on MySQL
framework(db_connection)

logger = ConsoleLogger()
# Log message from Logger Demo
framework(logger)
