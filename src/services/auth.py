class AuthService:
    def is_authenticated(
        self,
        *,
        session=None,
    ):
        exists = "user" not in session
        is_none = not session["user"]
        return exists or is_none
