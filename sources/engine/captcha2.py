"""
Captcha analyzer v2
"""

import os
import re

import requests
from PIL import Image


class WalkerCaptchaTpl(object):
    """ Класс объекта шаблона """

    __slots__ = ("memory",
                 "width",
                 "hotpoint",
                 "height",
                 "priority",
                 "number",
                 "count")

    def __init__(self, match: [], datadir: str, file: str):
        """ Конструктор """
        tmp_img = Image.open(datadir + file).convert("1")
        self.memory = tmp_img.load()
        self.width = tmp_img.width
        self.height = tmp_img.height
        self.priority = int(match[2])
        self.number = match[3]
        # Пересоберем сумму точек
        if not match[1]:
            self.count = self.calc()
            if self.count > 0:
                os.rename(datadir + file, datadir + "c%s_p%s_n%s.png" % (self.count, self.priority, self.number))
            else:
                raise ValueError("Bad tpl format")
        else:
            self.count = int(match[1])

    def calc(self):
        """ Подсчет количества пикселей"""
        tmp_cnt = 0
        tmp_y = 0
        while tmp_y < self.height:
            tmp_x = 0
            while tmp_x < self.width:
                tmp_cnt += self.memory[tmp_x, tmp_y] == 0
                tmp_x += 1
            tmp_y += 1
        # Вернем количество
        return tmp_cnt


class WalkerCaptcha(object):
    """ Captcha decoder """

    def __init__(self, filename: str):
        """ Конструктор """
        self.tpl = []
        self.sample = None
        self.load(filename)

    def load(self, path: str):
        """ Доступные шаблоны """
        for tmp_disk, tmp_dirs, tmp_files in os.walk(path):
            for tmp_file in tmp_files:
                tmp_match = re.match(r"(?:c(\d+)_)?(?:p(\d+)_)?n(\d+).png", tmp_file)
                if tmp_match:
                    self.tpl.append(WalkerCaptchaTpl(tmp_match, tmp_disk, tmp_file))
        # Шаблон фона
        self.sample = Image.open(path + "sample.png").load()

    def compare(self, src: [], dst: [], diff: int):
        """ Вхождение цвета в диапазон """
        tmp_a = src[0] - dst[0]
        if tmp_a < 0:
            tmp_a = -tmp_a
        tmp_b = src[1] - dst[1]
        if tmp_b < 0:
            tmp_b = -tmp_b
        tmp_c = src[2] - dst[2]
        if tmp_c < 0:
            tmp_c = -tmp_c
        return (tmp_a < diff) and (tmp_b < diff) and (tmp_c < diff)

    def clear(self, img: Image):
        """ Очистка от фона """
        img = img.crop((810, 540, 1310, 750))
        tmp_mem = img.load()
        tmp_width = img.width
        tmp_height = img.height
        # Параметры полотна
        tmp_white = (255, 255, 255)
        tmp_black = (0, 0, 0)
        tmp_max_y = 0
        tmp_min_y = tmp_height
        tmp_max_x = 0
        tmp_min_x = tmp_width
        # Пройдем по вертикали
        tmp_y = 0
        while tmp_y < tmp_height:
            tmp_x = 0
            while tmp_x < tmp_width:
                if not self.compare(tmp_mem[tmp_x, tmp_y], self.sample[tmp_x, tmp_y], 14):
                    tmp_mem[tmp_x, tmp_y] = tmp_black
                    if tmp_y < tmp_min_y:
                        tmp_min_y = tmp_y
                    elif tmp_x < tmp_min_x:
                        tmp_min_x = tmp_x
                    elif tmp_y > tmp_max_y:
                        tmp_max_y = tmp_y
                    elif tmp_x > tmp_max_x:
                        tmp_max_x = tmp_x
                else:
                    tmp_mem[tmp_x, tmp_y] = tmp_white
                tmp_x += 1
            tmp_y += 1
        # Обрежем найденную область
        img = img.crop((tmp_min_x, tmp_min_y, tmp_max_x, tmp_max_y))
        tmp_max_x = 300
        tmp_max_y = 60
        img.thumbnail((tmp_max_x, tmp_max_y), Image.CUBIC)
        # Сконвертируем в двухцветный
        return img.convert("L").point(lambda x: 255 if x == 255 else 0, mode='1')

    def fill(self, img: Image):
        """ Заполнение пустых точек в фигуре """
        tmp_mem = img.load()
        tmp_white = 255
        tmp_y = 1
        tmp_width = img.width - 1
        tmp_height = img.height - 1
        # Пройдем по вертикали
        while tmp_y < tmp_height:
            tmp_x = 1
            while tmp_x < tmp_width:
                cnt = 0
                if tmp_mem[tmp_x, tmp_y] != tmp_white:
                    tmp_x += 1
                    continue
                if tmp_mem[tmp_x - 1, tmp_y] != tmp_white:
                    cnt += 1
                if tmp_mem[tmp_x + 1, tmp_y] != tmp_white:
                    cnt += 1
                if tmp_mem[tmp_x, tmp_y - 1] != tmp_white:
                    cnt += 1
                if tmp_mem[tmp_x, tmp_y + 1] != tmp_white:
                    cnt += 1
                if tmp_mem[tmp_x - 1, tmp_y - 1] != tmp_white:
                    cnt += 1
                if tmp_mem[tmp_x + 1, tmp_y + 1] != tmp_white:
                    cnt += 1
                if tmp_mem[tmp_x - 1, tmp_y + 1] != tmp_white:
                    cnt += 1
                if tmp_mem[tmp_x + 1, tmp_y - 1] != tmp_white:
                    cnt += 1
                # У точки минимум 5 соседей
                if cnt > 4:
                    tmp_mem[tmp_x, tmp_y] = 0
                tmp_x += 1
            tmp_y += 1
        # Вернем память
        return tmp_mem

    def detect(self, img: Image):
        """ Заполнение пустых точек в фигуре """
        img = self.clear(img)
        tmp_mem = self.fill(img)
        tmp_val = ""
        # Размеры
        tmp_width = img.width - 1
        tmp_cipher = 0
        # Переберем все сиволы капчи
        while tmp_cipher < 5:
            tmp_found_tpl = None
            tmp_found_cnt = 0
            # Переберем все шаблоны
            for tmp_tpl in self.tpl:
                tmp_offset = -5
                tmp_max = 0
                tmp_cnt = 0
                while tmp_offset <= 20:
                    tmp_y = 0
                    while tmp_y < tmp_tpl.height:
                        tmp_x = 0
                        while tmp_x < tmp_tpl.width:
                            tmp_right = tmp_offset + tmp_x + tmp_cipher * 40
                            if tmp_right > tmp_width:
                                break
                            if tmp_mem[tmp_right, tmp_y] == 0 and tmp_tpl.memory[tmp_x, tmp_y] == 0:
                                tmp_cnt += 1
                            tmp_x += 1
                        # Новая строка
                        tmp_y += 1
                    # Корректирующее смещение
                    tmp_offset += 1
                    if tmp_cnt > tmp_max:
                        tmp_max = tmp_cnt
                    tmp_cnt = 0
                # Следующий шаблок
                tmp_delta = tmp_max / tmp_tpl.count
                if tmp_delta > tmp_found_cnt:
                    tmp_found_cnt = tmp_delta
                    tmp_found_tpl = tmp_tpl
            # Сумма по всем шаблонам
            if tmp_found_tpl:
                tmp_val += tmp_found_tpl.number
                tmp_cipher += 1
            else:
                return None
        # Вернем
        return tmp_val

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
