import os

SECRET_KEY = "alura"

URI_TEMPLATE = "{dbms}://{user}:{password}@{server}/{database}"
SQLALCHEMY_DATABASE_URI = URI_TEMPLATE.format(
    dbms="mysql+mysqlconnector",
    user="root",
    password="#Admin123",
    server="localhost",
    database="jogoteca",
)

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + "/uploads"
