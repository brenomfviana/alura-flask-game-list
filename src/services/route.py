from flask import redirect, url_for


class RouteService:
    def redirect(
        self,
        *_,
        redirect_page=None,
        next_page=None,
    ):
        return redirect(
            url_for(
                redirect_page,
                next=url_for(next_page),
            ),
        )
