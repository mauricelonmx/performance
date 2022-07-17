
import enum

class Config(enum.Enum):
    # Global constant
    PSQL_HOST = "localhost"
    PSQL_PORT = "5432"
    PSQL_USER = "postgres"
    PSQL_PASS = ""
    PSQL_DB = "test"
