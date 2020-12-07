"""
SQL Alchemy ORM example: schema creation and access both
user: postgres
password: postgres

"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# connect to the database
engine = create_engine('postgres://postgres:postgres@localhost/books')
Base = declarative_base()

# class representation of authors table
class Author(Base):
    __tablename__ = 'authors'

    author_id = Column(Integer, primary_key=True)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))

    def __repr__(self):
        return '''<Author(author_id='{0}', first_name='{1}', last_name='{2}')>'''.format(
            self.author_id, self.first_name, self.last_name)

# class representation of books table
class Book(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    number_of_pages = Column(Integer)

    def __repr__(self):
        return '''<Book(book_id='{0}', title='{1}', number_of_pages='{2}')>'''.format(
            self.book_id, self.title, self.number_of_pages)

# class representation of bookauthors table
class BookAuthor(Base):
    __tablename__ = 'bookauthors'

    bookauthor_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))

    def __repr__(self):
        return '''<BookAuthor(bookauthor_id='{0}', author_id='{1}', book_id='{2}')>'''.format(
            self.bookauthor_id, self.author_id, self.book_id)

    # relationship for SQLAlchemy classes
    author = relationship("Author")
    book = relationship("Book")

# create all the above tables using engine
Base.metadata.create_all(engine)

def create_session():
    Session = sessionmaker(bind=engine)
    return Session()


def add_book(title, number_of_pages, first_name, last_name):
    # create book record
    book = Book(title=title, number_of_pages=number_of_pages)

    session = create_session()

    try:
        existing_author = session.query(Author).filter(Author.first_name == first_name,
             Author.last_name == last_name).first()

        session.add(book)

        if existing_author is not None:
            session.flush()
            pairing = BookAuthor(author_id=existing_author.author_id,
                book_id = book.book_id)
        else:
            # create author record
            author = Author(first_name=first_name, last_name=last_name)
            session.add(author)
            session.flush()
            pairing = BookAuthor(author_id=author.author_id, book_id=book.book_id)
            
        session.add(pairing)
        session.commit()

    except:
        session.rollback()
        raise
    finally:
        session.close()



if __name__ == '__main__':
    print("Input new book!")
    title = input("What's the book name?\n")
    number_of_pages = int(input("How many pages are in the book?\n"))
    first_name = input("What is the first name of the author?\n")
    last_name = input("What is the last name of the author?")
    add_book(title, number_of_pages, first_name, last_name)
    print("Done!")
