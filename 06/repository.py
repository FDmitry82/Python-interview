"""Репозиторий (скрипт управления хранилищем данных)"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_path = 'db.sqlite3'


class Repository:
    """Репозиторий"""

    def __init__(self, db_path):
        self.engine = create_engine(f'sqlite:///{db_path}?check_same_thread=False')
        self.create_base()
        self.session = self.get_session()

    def create_base(self):
        """Создаем БД"""
        base = declarative_base()
        base.metadata.create_all(self.engine)

    def get_session(self):
        """Создаем объект сессии"""
        session = sessionmaker(bind=self.engine)
        session = session()
        return session


if __name__ == '__main__':
    REP = Repository(db_path)
