import os

DATABASE_URL = os.getenv("DATABASE_URL", "mysql://app:app@localhost:3306/app")
ORM = "Tortoise ORM"
DATABASE = "MariaDB"
REST_ONLY = True
