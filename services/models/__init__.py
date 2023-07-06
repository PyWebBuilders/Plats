import os

from bframe import Frame
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

Base = declarative_base()


def init_app(app: Frame):
    db_type = app.Config.get("SQLALCHEMY_DATABASE_TYPE")
    db_db = app.Config.get("SQLALCHEMY_DATABASE_DB")

    SQLALCHEMY_DATABASE_URI = "%s:///%s" % (db_type, db_db)
    engine = create_engine(SQLALCHEMY_DATABASE_URI,
                           echo=app.Config.get("DEBUG"))

    global Session
    Session = scoped_session(sessionmaker(engine))

    if not os.path.exists(db_db):
        from services.models.users import init_db
        init_db(app, engine, Session)