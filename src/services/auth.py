class AuthService:
    def is_authenticated(
        self,
        *,
        session=None,
    ):
        exists = "user" in session
        is_none = exists and not session["user"]
        return not exists or is_none
