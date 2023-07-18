from services.models import Base
from sqlalchemy import Integer, Column, String
from sqlalchemy import TEXT

from services.utils.static import code_type_py


class Code(Base):
    __tablename__ = 'codes'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    uid = Column(Integer(), comment="用户")
    name = Column(String(100), comment='标题')
    content = Column(TEXT(), comment='内容')
    code_type = Column(String(1), comment="代码类型")
    state = Column(String(1), default=1, comment="状态")


def init_db(app, engine, Session):
    Base.metadata.create_all(engine)

    if app.Config.get("DEBUG"):
        # 开发模式下 插入一些简单的数据
        with Session() as session:
            session.add_all([
                Code(uid=1, name="py代码001",
                     content="print(\"hello world\")", code_type=code_type_py()),
                Code(uid=1, name="py代码002",
                     content="print(\"hello python!\")", code_type=code_type_py()),
            ])
            session.commit()
