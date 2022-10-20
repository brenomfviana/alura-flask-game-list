import os
import time

from app import app


class ImageService:
    DEFAULT_COVER = "default_cover.jpg"
    UPLOAD_PATH = "UPLOAD_PATH"

    def get_image(
        self,
        *_,
        id=None,
    ) -> str:
        target = f"capa{id}"
        for name in os.listdir(app.config[self.UPLOAD_PATH]):
            if target in name:
                return name
        return self.DEFAULT_COVER

    def add(
        self,
        *_,
        picture=None,
        game=None,
    ) -> None:
        self.__delete_image(id=game.id)
        picture_name = self.__new_name(id=game.id)
        picture.save(picture_name)

    def __delete_image(
        self,
        *_,
        id=None,
    ) -> None:
        image = self.get_image(id=id)
        if image != self.DEFAULT_COVER:
            os.remove(os.path.join(app.config[self.UPLOAD_PATH], image))

    def __new_name(
        self,
        *_,
        id=None,
    ) -> str:
        path = app.config[self.UPLOAD_PATH]
        timestamp = time.time()
        return f"{path}/capa{id}-{timestamp}.jpg"
