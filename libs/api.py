from sqlalchemy import or_

from libs.helpers import persist

from models.model import (Person, Group, EmailAddress,
                          AddressBook, AddressBookPerson,
                          AddressBookGroup)


def get_person_groups(session, person_id):
    """ Returns a list of Group objects that Person belongs to based
        on person_id """
    return session.query(Person)\
        .filter(Person.id == person_id)\
        .one()\
        .groups


def get_group_members(session, group_id):
    """ Returns a list of Person objects that belong to Group
        based on group_id """
    return session.query(Group)\
        .filter(Group.id == group_id)\
        .one()\
        .members


def get_person_by_name(session, name):
    """ Returns a Person object based on name """
    return session.query(Person)\
        .filter(or_(Person.first_name == name,
                    Person.last_name == name,
                    Person.full_name == name))\
        .first()


def get_person_by_email(session, email_address):
    """ Returns a Person object based on email_address """
    return session.query(Person)\
        .join(EmailAddress)\
        .filter(EmailAddress.email.like('{}%'.format(email_address)))\
        .first()


def add_person_to_address_book(session, person_id):
    """ Adds a person to an AddressBookPerson based on person_id """
    address_book = AddressBook()
    persist(session, address_book)
    address_book_person = AddressBookPerson()
    address_book_person.person_id = person_id
    address_book_person.address_book_id = address_book.id
    persist(session, address_book_person)
    session.commit()


def add_group_to_address_book(session, group_id):
    """ Adds a group to an AddressBookGroup based on group_id """
    address_book = AddressBook()
    persist(session, address_book)
    address_book_group = AddressBookGroup()
    address_book_group.group_id = group_id
    address_book_group.address_book_id = address_book.id
    persist(session, address_book_group)
    session.commit()
