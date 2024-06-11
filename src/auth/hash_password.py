from typing import Optional


from fastapi_users.password import PasswordHelperProtocol, PasswordHelper


class PasswordConfigurator:
    password_for_hash = "ssh"
    password_helper: PasswordHelperProtocol

    def __init__(
            self,
            password_helper: Optional[PasswordHelperProtocol] = None,
    ):
        if password_helper is None:
            self.password_helper = PasswordHelper()
        else:
            self.password_helper = password_helper

    def hashh(self, password_for_hash):
        hashed_password = self.password_helper.hash(self.password_for_hash)
        return hashed_password


last_ekz = PasswordConfigurator()