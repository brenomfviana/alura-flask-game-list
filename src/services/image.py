import os

from app import app


class ImageService:
    def get_image(
        self,
        *_,
        id=None,
    ):
        target = f"capa{id}.jpg"
        for name in os.listdir(app.config["UPLOAD_PATH"]):
            if name == target:
                return name
        return "default_cover.jpg"
