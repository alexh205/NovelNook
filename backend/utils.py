import bcrypt


def set_password(password):
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return password


def check_password(password, db_password):
    return bcrypt.checkpw(password.encode("utf-8"), db_password)
