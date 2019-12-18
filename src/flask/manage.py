from thermos import app, db
from flask_script import Manager, prompt_bool

manager = Manager(db)


@manager.command
def initdb():
    db.create_all()
    print("Initialized the database")


@manager.command
def dropdb():
    if prompt_bool("are you sure to delete database?"):
        db.drop_all()
        print("Dropped the database")


if __name__ == '__main__':
    manager.run()
