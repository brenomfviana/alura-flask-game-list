from constants import ID_KEY, NEXT_PAGE_KEY
from flask import redirect, url_for


class RedirectService:
    INDEX_PAGE = "index"
    LOGIN_PAGE = "login"

    def __redirect(
        self,
        *_,
        page=None,
        next_page=None,
        id=None,
    ):
        assert page != None

        kwargs = {}

        if next_page:
            kwargs[NEXT_PAGE_KEY] = next_page

        if id:
            kwargs[ID_KEY] = id

        return redirect(
            url_for(
                page,
                **kwargs,
            ),
        )

    def to_page(
        self,
        *_,
        page=None,
        id=None,
    ):
        assert page != None

        return self.__redirect(
            page=page,
            id=id,
        )

    def to_login(
        self,
        *_,
        next_page=None,
        id=None,
    ):
        return self.__redirect(
            page=self.LOGIN_PAGE,
            next_page=next_page,
            id=id,
        )

    def to_index(self):
        return self.to_page(
            page=self.INDEX_PAGE,
        )
