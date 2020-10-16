from ..models.basic_models_no_comments import User, session


def run_get_all_rows_from_table():
    # iterator version
    for row in session.query(User):
        print('iterative:', row)

    # list version
    all_rows: list = session.query(User).all()
    for row in all_rows:
        print('list version:', row)
