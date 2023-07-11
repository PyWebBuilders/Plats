from services.models import Base
from sqlalchemy import Integer, Column, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True, index=True, comment='用户名')
    password = Column(String(100), nullable=False, comment='密码')
    email = Column(String(20), index=True, comment='邮箱')
    role = Column(String(1), comment="角色")
    state = Column(String(1), default=1, comment="状态")


def init_db(app, engine, Session):
    Base.metadata.create_all(engine)

    if app.Config.get("DEBUG"):
        # 开发模式下 插入一些简单的数据
        with Session() as session:
            session.add_all([
                User(username="admin", password="admin", email="admin@admin.com", role=1),
                User(username="tom", password="tom", email="tom@tom.com", role=2),
                User(username="jerry", password="jerry", email="jerry@jerry.com", role=2)
            ])
            session.commit()
