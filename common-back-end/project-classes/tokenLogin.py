class TokenLogin:

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def _is_valid_user_name(self, user_name):
        if len(user_name) > 30:
            raise ValueError("User Name cannot exceed 30 characters.")
        return user_name

    def _is_valid_password(self, password):
        if len(password) > 30:
            raise ValueError("Password cannot exceed 30 characters.")
        return password
