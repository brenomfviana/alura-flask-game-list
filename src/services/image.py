import os
import time

from app import app


class ImageService:
    DEFAULT_COVER = "default_cover.jpg"

    def new_name(
        self,
        *_,
        id=None,
    ) -> str:
        path = app.config["UPLOAD_PATH"]
        timestamp = time.time()
        return f"{path}/capa{id}-{timestamp}.jpg"

    def get_image(
        self,
        *_,
        id=None,
    ) -> str:
        target = f"capa{id}"
        for name in os.listdir(app.config["UPLOAD_PATH"]):
            if target in name:
                return name
        return self.DEFAULT_COVER

    def delete_image(
        self,
        *_,
        id=None,
    ) -> None:
        image = self.get_image(id=id)
        if image != self.DEFAULT_COVER:
            os.remove(os.path.join(app.config["UPLOAD_PATH"], image))
