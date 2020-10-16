from sqlalchemy import exists

from ..models.basic_models_no_comments import session, User

_usernames = ('james', 'jones', 'bob', 'jenna', 'scott')


def run_insert_into_table():
    for username in _usernames:
        # check if the name already exists
        if not session.query(exists().where(User.username == username)).scalar():
            # add the new User to the queue to be executed
            session.add(User(username=username))
    # push the changes to the database
    session.commit()
