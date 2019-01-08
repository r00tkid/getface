from django.contrib.auth.models import User


def password_validation(password, password_confirmation, user_data):
    error = {}
    user = None

    if not password.__eq__(password_confirmation):
        error['mismatch'] = 'Passwords not match'

    if len(password) < 6:
        error['min'] = 'Minimum password length is 6'

    if len(password) > 100:
        error['max'] = 'Maximum password length is 100'

    if password in user_data.values():
        error['similarity'] = 'Password can not be similar to other fields'

    if not bool(error):
        user = User(**user_data)
        user.set_password(password)

    return user, error if bool(error) else None
