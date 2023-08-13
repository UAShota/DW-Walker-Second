"""
Captcha analyzer v1
"""

import os

import requests
from PIL import Image


class WalkerCaptchaTpl(object):
    """ Класс объекта шаблона """

    __slots__ = ("memory",
                 "width",
                 "hotpoint")

    def __init__(self, filename: str):
        """ Конструктор """
        tmp_img = Image.open(filename)
        self.memory = tmp_img.load()
        self.width = tmp_img.width
        self.hotpoint = self.memory[0, 0]


class WalkerCaptcha(object):
    """ Captcha decoder """

    def __init__(self, filename: str):
        """ Конструктор """
        self.tpl = []
        self.load(filename)

    def load(self, path: str):
        """ Вхождение цвета в диапазон """
        for tmp_disk, tmp_dirs, tmp_files in os.walk(path):
            for tmp_file in tmp_files:
                self.tpl.append(WalkerCaptchaTpl(path + tmp_file))
        return

    def colorize(self, src: [], dst: [], diff: int = 40):
        """ Вхождение цвета в диапазон """
        return abs(src[0] - dst[0]) < diff and abs(src[1] - dst[1]) < diff and abs(src[2] - dst[2]) < diff

    def mynameis(self, w: int, h: int, x: int, y: int):
        """ Определение имени капчи """
        if x < w / 3:
            x = 0
        elif x < w / 2:
            x = 1
        else:
            x = 2
        # По горизонтали
        if y < h / 3:
            y = 0
        elif y < h / 2:
            y = 1
        else:
            y = 2
        # Поименуем
        tmp_names = {"00": "enhp",
                     "10": "troph",
                     "20": "fish",
                     "01": "orden",
                     "11": "stam",
                     "21": "ensz",
                     "02": "injur",
                     "12": "depth",
                     "22": "kills"}
        return tmp_names["%s%s" % (x, y)]

    def detect(self, img: Image):
        """ Детект капчи """
        tmp_mem = img.load()
        # Размеры
        tmp_width = img.width
        tmp_height = img.height
        tmp_jump_x = int(tmp_width / 6)
        tmp_jump_y = int(tmp_height / 6)
        # Точки отсчета
        tmp_y = int(tmp_jump_y / 2)
        # Пройдем по вертикали
        while tmp_y < tmp_height - tmp_jump_y:
            # Перепрыгнем заранее пустое место
            if tmp_y > 0 and tmp_y % tmp_jump_y == 0:
                tmp_y += tmp_jump_y
            # Первая точка со сдвигом от края
            tmp_x = int(tmp_jump_x / 2)
            while tmp_x < tmp_width - tmp_jump_x:
                # Перепрыгнем заранее пустое место
                if tmp_x > 0 and tmp_x % tmp_jump_x == 0:
                    tmp_x += tmp_jump_x
                    # Проверим горячую точку
                tmp_color = tmp_mem[tmp_x, tmp_y]
                # Переберем все шаблоны
                for tmpTpl in self.tpl:
                    if not self.colorize(tmp_color, tmpTpl.hotpoint):
                        continue
                    # Проверим остальные точки
                    tmp_skip = False
                    for tmp_offset in range(1, tmpTpl.width):
                        if self.colorize(tmp_mem[tmp_x + tmp_offset, tmp_y], tmpTpl.memory[tmp_offset, 0]):
                            pass
                        else:
                            tmp_skip = True
                            break
                    if not tmp_skip:
                        return self.mynameis(tmp_width, tmp_height, tmp_x, tmp_y)
                # Новый столбец
                tmp_x += 1
            # Новая строка
            tmp_y += 1
        # Вернем
        return None

    def fromurl(self, url: str):
        """ Распознавание капчи в файле по ссылке """
        tmp_raw = requests.get(url, stream=True).raw
        if tmp_raw:
            return self.detect(Image.open(tmp_raw))
        else:
            return None

    def fromfile(self, path: str):
        """ Распознавание капчи в файле """
        return self.detect(Image.open(path))
