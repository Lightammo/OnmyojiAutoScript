# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import numpy as np

from module.atom.image import RuleImage
from module.logger import logger


class ImageGrid:

    def __init__(self, images: list[RuleImage]):
        self.images = images

    def find_anyone(self, img: np.array) -> RuleImage or None:
        """
        在这些图片中找到其中一个
        :param img:
        :return: 如果没有找到返回None
        """
        for image in self.images:
            if image.match(img):
                return image
        return None

    def find_all_img(self, img: np.array):
        images = []
        for image in self.images:
            matched = image.match_all(img)
            images.extend(matched)
        location = []
        for matched in images:
            score, x, y, w, h = matched
            center_x, center_y = int(x + w // 2), int(y + h // 2)
            location.append(
                (center_x, center_y)
            )

        images.sort(key=lambda i: i[1])
        logger.info(f"Target matches with {images}")
        return location
