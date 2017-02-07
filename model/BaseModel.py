from peewee import *

from set_connection import SetConnection

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop

connected = SetConnection()

db = PostgresqlDatabase(connected.username, user=connected.username)
db = SqliteDatabase('my_app.db')

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db