DEBUG = True
WSGI_MODE = False

HOST = "0.0.0.0"
PORT = 7256

SECURE_KEY = "Plats"

SQLALCHEMY_DATABASE_TYPE = "sqlite"
SQLALCHEMY_DATABASE_DB = "plats.db"


# token expires
TOEKN_EXPIRE = 30 * 60  # 30分钟