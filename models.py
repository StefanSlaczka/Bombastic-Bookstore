from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from werkzeug.security import generate_password_hash, check_password_hash
from web_app_main import db
from flask_login import UserMixin
# from web_app_main import login


# This loads the user ID from the User db on log in
# It also seems to be related to the circular import issue
# @login.user_loader
# def load_user(user_id):
    # return db.session.query(User).get(int(user_id))


# This is what populates the User db when the migration script is generated
# The migration script is generated by entering [flask db migrate -m "user table"] into the Python terminal
# (without brackets)
# To apply changes to the db from the migration script, [flask db upgrade] in the Python terminal
# (again without brackets)
# the script generation & upgrade must also be done when changes are made to the User db
# Function establishes fields as class variables
# These will be the columns in the User db

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(128), index=True,
                                             unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # These use the Werkzeug core dependency for password hashing/checking
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)
