from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship


Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    groups = relationship("Group", backref='Group', uselist=True)
    emails = relationship("EmailAddress", backref='EmailAddress', uselist=True)

    @hybrid_property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class StreetAddress(Base):
    __tablename__ = "street_address"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey(Person.id), nullable=False)


class EmailAddress(Base):
    __tablename__ = "email_address"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(Integer, ForeignKey(Person.id), nullable=False)


class PhoneNumber(Base):
    __tablename__ = "phone_number"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey(Person.id), nullable=False)


class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey(Person.id), nullable=True)
    members = relationship("Person", backref='Person', uselist=True)


class AddressBook(Base):
    __tablename__ = "address_book"
    id = Column(Integer, primary_key=True)


class AddressBookPerson(Base):
    __tablename__ = "address_book_person"
    person_id = Column(Integer, ForeignKey(Person.id), primary_key=True)
    address_book_id = Column(Integer, ForeignKey(AddressBook.id),
                             primary_key=True)


class AddressBookGroup(Base):
    __tablename__ = "address_book_group"
    group_id = Column(Integer, ForeignKey(Group.id), primary_key=True)
    address_book_id = Column(Integer, ForeignKey(AddressBook.id),
                             primary_key=True)
