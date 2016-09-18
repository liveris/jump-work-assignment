from models.model import Person, Group, EmailAddress


def create_person(_id, first_name, last_name):
    p = Person()
    p.id = _id
    p.first_name = first_name
    p.last_name = last_name
    return p


def create_group(_id, person_id=None):
    g = Group()
    g.id = _id
    g.person_id = person_id
    return g


def create_email_address(email, person_id):
    e = EmailAddress()
    e.email = email
    e.person_id = person_id
    return e


def persist(session, object_):
    session.add(object_)
    session.flush()
