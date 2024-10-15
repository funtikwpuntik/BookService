from domain.db_tables import Book
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, select, delete, update
from sqlalchemy.orm import sessionmaker
class SQLiteStorage:


    def __init__(self):
        self.Session =  sessionmaker(create_engine("sqlite+pysqlite:///test.db", echo=True))
        self.session = self.Session()


    def add(self, book):
        self.session.add(book)
        self.session.commit()

        self.session.refresh(book)
        print(book)

        # Теперь можно получить id
        data = {
            "id": book.id,
            "data":
                {"title": book.title,
                 "description": book.description,
                 "publish_year": book.publish_year,
                 "pages_count": book.pages_count,
                 "created_at": book.created_at, }
        }
        return data

    def delete(self, id):
        self.session.execute(delete(Book).where(Book.id == id))
        self.session.commit()
        return {}

    def update(self, id, data):
        self.session.execute(
            update(Book).
            where(Book.id == id).
            values(
                title=data['title'],
                description=data['description'],
                publish_year=data['publish_year'],
                pages_count=data['pages_count'],
        ))
        self.session.commit()
        return {}

    def get(self):
        books = self.session.execute(select(Book)).scalars()
        data = [i.as_dict() for i in books]
        return data