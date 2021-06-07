# coding: utf-8
from sqlalchemy import Column, String, TIMESTAMP, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TUser(Base):
    __tablename__ = 't_user'
    __table_args__ = {'comment': '用户表'}

    id = Column(INTEGER(11), primary_key=True, comment='无关逻辑的主键')
    username = Column(String(32), nullable=False, server_default=text("''"), comment='用户名')
    enable = Column(INTEGER(11), nullable=False, server_default=text("'1'"), comment='1的时候可用，为0的时候账号不可用')
    create_time = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"), comment='创建时间')
