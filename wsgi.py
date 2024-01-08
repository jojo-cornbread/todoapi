import click
from models import db
from flask.cli import with_appcontext, AppGroup
from main import app
from models import User, Todo

'''
Generic Commands
'''

@app.cli.command("init")
def initialize():
    db.drop_all()
    db.create_all()

    bob = User("bob", "bob@mail.com", "bobpass")
    rick = User("rick", "rick@mail.com", "rickpass")
    db.session.add_all([bob, rick])
    db.session.commit()
    print('database intialized')

# basic cli commands for testing
@app.cli.command('get_users', help='lists all users in db')
def list_users_command():
    users = User.query.all()
    print(users)

@app.cli.command("run")
def initialize():
    app.run(host='0.0.0.0', port=8080, debug=True)
