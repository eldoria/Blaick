from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from metadata import metadata

db_string = "postgresql://sdvdvqdmhxupyf:387e889dac2222494bfb1cefe9b691ad343868a191e348346c9cc20c647dee1e@ec2-34-255-134-200.eu-west-1.compute.amazonaws.com:5432/detbm6rt4rrcu4"
engine = create_engine(db_string, echo=False)
# Session = sessionmaker(bind=engine)

session = Session(engine)

Base = declarative_base()

'''
def create_table(table: Table):
    table.create(engine)
    inspector = inspect(engine)


def delete_table(table: Table):
    table.drop(engine)
    inspector = inspect(engine)
'''


def check_if_data_exist(table, field, value):
    q = session.query(table).filter(field == value)
    response = session.query(q.exists()).scalar()
    return response


def insert_data_without_duplicates(obj, table, field, value):
    response = check_if_data_exist(table, field, value)
    if not response:
        insert_data(obj)
        return True
    else:
        return False


def insert_data(obj: object):
    with session as ses:
        ses.add(obj)
        ses.commit()
    print('insert new line into database')


if __name__ == '__main__':
    metadata.create_all(engine)

