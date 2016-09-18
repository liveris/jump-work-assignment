# API assignment
### Features

To add a person to the address book, use the add_person_to_address_book function with parameters a working sqlalchemy session and the person id.

To add a group to the address book, use the add_group_to_address_book function with parameters a working sqlalchemy session and the group id.

To find the members of the group, use the get_group_members function with parameters a working sqlalchemy session and the group id.

To find the groups a person belong to, use the get_person_groups with parameters a working sqlalchemy session and the person id.

To find a person by name (can supply either first name, last name, or both), use the get_person_by_name function with parameters a working sqlalchemy session and the person's name.

To find a person by the full e-mail address or any prefix of that, use the get_person_by_email function with parameters a working sqlalchemy session and the person's email string.

### Design - only question

I am not sure I understand how different is this question from the latest feature requirement. I would make a like query (%email_string%) to the email sting to achive this. The question says to assume that the address book has an email address which is not in the feature requirements. Only the person has an email address. If we assume that the address book has an extra attribute email address, I would make a join between the AddressBook, AddressBookPerson and Person and then a like query.

## Getting Started

The api can be imported from libs/api.py. 

### Prerequisities

Sqlalchemy needs to be installed. After having installed it, you need an sqlalchmey session
to pass as a parameter to the api functions.  

## Running the tests
 To run the unittests execute
 python3 -m unittest tests/test.py
