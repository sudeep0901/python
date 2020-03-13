from thermos import app, db
# from thermos.models import User
from flask_script import Manager, prompt_bool

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="sudeep", email="sudeep@gmail.com"))
    db.session.commit()
    print("Initialized the database")


@manager.command
def dropdb():
    if prompt_bool("are you sure to delete database?"):
        db.drop_all()
        print("Dropped the database")


if __name__ == '__main__':
    manager.run()
