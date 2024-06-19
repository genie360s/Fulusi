import os
import psycopg
import click
from flask import current_app, g 
from dotenv import load_dotenv

load_dotenv()
"""
g is a special object that is unique for each request. It is used to store data that 
might be accessed by multiple functions during the request. The connection is stored
and reused instead of creating a new connection if get_db is called a second time in the same request.

current_app is another special object that points to the Flask application
handling the request. Since you used an application factory, 
there is no application object when writing the rest of your code. 
get_db will be called when the application has been created and is 
handling a request, so current_app can be used.

psycopg is a PostgreSQL database adapter for the Python programming language.

load_dotenv() loads environment variables from a .env file into os.environ.

close_db checks if a connection was created by checking if g.db was set. 
If the connection exists, it is closed. Further down you will tell your 
application about the close_db function in the application factory so 
that it is called after each request.
"""

def get_db():
    if 'db' not in g:
        g.db = psycopg.connect(
            host=os.getenv('DB_HOST'),
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        g.db.autocommit = True

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
"""
click.command() defines a command line command called init-db that calls 
the init_db function and shows a success message to the user. You can read 
Command Line Interface to learn more about writing commands.
"""
def init_db():
    db = get_db()

    with current_app.open_resource('user_schema.sql') as f:
        cursor = db.cursor()
        schema_sql = f.read().decode('utf8')
        commands = schema_sql.split(';')
        for command in commands:
            if command.strip():
                cursor.execute(command)
        cursor.close()

@click.command('init-db')
def init_db_command():
    """Clear the user table and create new user table"""
    init_db()
    click.echo('Created the user table.')

"""
app.teardown_appcontext() tells Flask to call that function when cleaning up after 
returning the response.

app.cli.add_command() adds a new command that can be called with the flask command.
"""

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
