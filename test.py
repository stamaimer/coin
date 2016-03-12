from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://stamaimer:123456@192.168.0.103/coin", echo=True)

Base = declarative_base()

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    username = Column(String)

    password = Column(String)

    def __repr__(self):

        return "<User(id=%d, username='%s', password='%s')>" % (self.id,
                                                                self.username,
                                                                self.password)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

user = User(username="stamaimer", password="123456")

session.add(user)

result = session.query(User).filter_by(username="stamaimer").first()

print result

print result is user

# session.rollback()
