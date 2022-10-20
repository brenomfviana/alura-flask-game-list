from flask import redirect, url_for


class RedirectService:
    INDEX_PAGE = "index"
    LOGIN_PAGE = "login"

    def __redirect(
        self,
        *_,
        redirect_page=None,
        next_page=None,
    ):
        assert redirect_page != None

        if not next_page:
            return redirect(
                url_for(redirect_page),
            )

        return redirect(
            url_for(
                redirect_page,
                next=next_page,
            ),
        )

    def to_index(self):
        return self.__redirect(
            redirect_page=self.INDEX_PAGE,
        )

    def to_login(
        self,
        *_,
        next_page=None,
    ):
        return self.__redirect(
            redirect_page=self.LOGIN_PAGE,
            next_page=next_page,
        )

    def to_page(
        self,
        *_,
        page=None,
    ):
        return self.__redirect(
            redirect_page=page,
        )
