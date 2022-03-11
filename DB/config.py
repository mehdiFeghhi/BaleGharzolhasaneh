import os


class DbConfig:
    db_user = os.getenv('POSTGRES_USER', "postgres")
    db_password = os.getenv('POSTGRES_PASSWORD', "myPassword")
    db_host = os.getenv('POSTGRES_HOST', "localhost")
    # db_name = os.getenv('POSTGRES_DB', "postgres@localhost")
    db_name = os.getenv('POSTGRES_DB', "postgres")
    db_port = os.getenv('POSTGRES_PORT', "5432")
    database_url = "postgresql://{}:{}@{}:{}/{}".format(db_user, db_password, db_host, db_port, db_name) or None
    # database_url = "jdbc:postgjdbc:resql://localhost:5432/postgres"