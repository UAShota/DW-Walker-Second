"""
Some classes
"""

import urllib.parse


class WalkerFight(object):
    """ Класс состояния боевки """

    def __init__(self):
        """ Конструктор """
        # Признак первого хода
        self.isInit = False
        # Признак возможности смены стойки
        self.isStand = False
        # Признак элитного противника
        self.isElite = False
        # Признак хранителя
        self.isKeeper = False
        # Признак пвп
        self.isPVP = False
        # Признак брошенного перемирия
        self.isPeace = False
        # Гильдия противника
        self.enemyGuild = ""
        # Атака противника
        self.enemyAttack = 0
        # Броня противника
        self.enemyArmor = 0
        # Размер противника
        self.enemySize = 0
        # Текущее хп противника
        self.enemyLoHp = 0
        # Полное хп противника
        self.enemyHiHp = 0
        # Реген противника
        self.enemyRegen = 0
        # Процент хп противника
        self.enemyPercent = 0
        # Точность игрока
        self.myAccuracy = 0
        # Концентрация игрока
        self.myConcentration = 0
        # Текущее хп игрока
        self.myLoHp = 0
        # Полное хп игрока
        self.myHiHp = 0
        # Реген игрока
        self.myRegen = 0
        # Процент хп игрока
        self.myPercent = 0
        # Наличие сумки на поясе
        self.myBag = True
        # Текущая или устанавливаемая стойка
        self.myStand = ""


class SellerItem:
    """ Предмет продажи """

    __slots__ = ("id",
                 "name",
                 "action")

    def __init__(self):
        """ Конструктор """
        self.id = 0
        self.name = ""
        self.action = 0


class AUHelper:
    """ Activ Users helper """

    @staticmethod
    def buildQuery(data):
        """ Build PHP Array from JS Array """
        m_parents = list()
        m_pairs = dict()

        def renderKey(parents: list):
            """ Key decoration """
            depth, out_str = 0, ''
            for x in parents:
                s = "[%s]" if depth > 0 or isinstance(x, int) else "%s"
                out_str += s % str(x)
                depth += 1
            return out_str

        def r_urlencode(rawurl: str):
            """ Encode URL """
            if isinstance(rawurl, list) or isinstance(rawurl, tuple):
                for tmp_index in range(len(rawurl)):
                    m_parents.append(tmp_index)
                    r_urlencode(rawurl[tmp_index])
                    m_parents.pop()
            elif isinstance(rawurl, dict):
                for tmp_key, tmp_value in rawurl.items():
                    m_parents.append(tmp_key)
                    r_urlencode(tmp_value)
                    m_parents.pop()
            else:
                m_pairs[renderKey(m_parents)] = str(rawurl)
            return m_pairs

        return urllib.parse.urlencode(r_urlencode(data))

    @staticmethod
    def buildHeaders(length: int, referer: str):
        """ Request header """
        tmp_params = {
            'Host': 'vip3.activeusers.ru',
            'Connection': 'keep-alive',
            'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'DNT': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://vip3.activeusers.ru',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': referer,
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        if length > 0:
            tmp_params['Content-Length'] = str(length)
        # Completed array
        return tmp_params
