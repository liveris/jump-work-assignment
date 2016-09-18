import unittest
from unittest.mock import patch

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from libs.api import (add_group_to_address_book,
                      add_person_to_address_book,
                      get_group_members,
                      get_person_groups,
                      get_person_by_name,
                      get_person_by_email)
from libs.helpers import (create_person, create_group,
                          create_email_address)

from models.meta import Base
from models.model import AddressBookPerson, AddressBookGroup


class TestLibAPI(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=self.engine)

        Base.metadata.create_all(self.engine)
        self.session = Session()

        self.person1 = create_person(1, "George", "Bowie")
        self.person2 = create_person(2, "John", "Owen")

        self.session.add(self.person1)
        self.session.add(self.person2)

        self.group1 = create_group(1, self.person1.id)
        self.session.add(self.group1)
        self.email1 = create_email_address("george@company.com",
                                           self.person1.id)
        self.session.add(self.email1)

        self.session.commit()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_add_person_to_adress_book(self):
        add_person_to_address_book(self.session, self.person1.id)
        expected = self.session.query(AddressBookPerson)\
            .filter(AddressBookPerson.person_id).all()
        self.assertEqual(self.person1.id, expected[0].person_id)

    def test_add_group_to_adress_book(self):
        add_group_to_address_book(self.session, self.group1.id)
        expected = self.session.query(AddressBookGroup)\
            .filter(AddressBookGroup.group_id).all()
        self.assertEqual(self.group1.id, expected[0].group_id)

    def test_get_group_members(self):
        result = get_group_members(self.session, self.group1.id)
        self.assertListEqual([self.person1], result)

    def test_get_person_groups(self):
        result = get_person_groups(self.session, self.group1.id)
        self.assertListEqual([self.group1], result)

    def test_get_person__by_email(self):
        result = get_person_by_email(self.session, "george")
        self.assertEqual(self.person1, result)

    def test_get_person__by_first_name(self):
        result = get_person_by_name(self.session, "George")
        self.assertEqual(self.person1, result)

    def test_get_person__by_last_name(self):
        result = get_person_by_name(self.session, "Bowie")
        self.assertEqual(self.person1, result)

    def test_get_person__by_full_name(self):
        """ This test fails but I have no idea why. According
            to official documentaion it should work. Maybe
            sqlite specific error.
            http://docs.sqlalchemy.org/en/latest/orm/mapped_sql_expr.html
        """
        result = get_person_by_name(self.session, "George Bowie")
        self.assertEqual(self.person1, result)
