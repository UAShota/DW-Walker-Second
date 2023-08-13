"""
Trade bot module
"""

from .engine import *


class TraderItem:
    """ Предмет торговли """

    __slots__ = ("name",
                 "cost",
                 "limit",
                 "guild")

    def __init__(self):
        """ Конструктор """
        self.name = ""
        self.cost = 0
        self.limit = 0
        self.guild = False


class Trader(Engine):
    """ Движок обработки торговли """

    # Текущая версия
    VERSION = 2.02

    # Идентификатор торгового бота
    TRADE_BOT_ID = -183040898

    # Идентификатор игрового бота
    GAME_BOT_ID = -182985865

    def __init__(self, config: any, name: str, send: callable = None, lock: object = None):
        """ Конструктор """
        self.items = {}
        self.regView = self.compile(r"^⚖(.+) выставляет на аукцион \((\d+)\).+?(\d+)\*(.+) - (\d+) золота")
        self.regAccept = self.compile(r"^⚖.+Вы успешно приобрели с аукциона предмет (\d+)\*(.+) -")
        # Создадим базовый класс
        super().__init__(config(self.register), name, lock)
        # Перенаправление покупки
        if send:
            self.send = send
        # Готово
        self.log("Trader v%s" % self.VERSION)
        self.thread(self.check)

    def register(self, name: str, cost: int, limit: int, guild: bool):
        """ Регистрация закупки """
        tmp_item = TraderItem()
        tmp_item.name = name
        tmp_item.cost = cost
        tmp_item.limit = limit
        tmp_item.guild = guild
        # Добавим в наш списочек
        self.items[name] = tmp_item

    def check(self):
        """ Проверка текущего сообщения """
        if self.buy():
            return
        if self.trade():
            return

    def buy(self):
        """ Покупка """
        if not self.event.from_chat:
            return False
        if self.event.user_id != self.TRADE_BOT_ID:
            return False
        # Пробьем регулярку
        tmp_match = self.regView.search(self.event.message)
        if not tmp_match:
            return False
        # Попытка покупки
        tmp_user = tmp_match[1]
        tmp_lot = tmp_match[2]
        tmp_count = int(tmp_match[3])
        tmp_name = tmp_match[4].lower()
        tmp_cost = int(tmp_match[5])
        # Поищем, нужен ли он нам
        if not not (tmp_name in self.items):
            return True
        # Вытащим
        tmp_item = self.items[tmp_name]
        # Лимит
        if tmp_item.limit < tmp_count:
            return True
        # Цена
        if tmp_item.cost >= int(tmp_cost / tmp_count):
            self.log("Лот %s запрос %s %s за %s у %s" % (tmp_lot, tmp_count, tmp_name, tmp_cost, tmp_user))
            self.send("Купить лот %s" % tmp_lot, self.GAME_BOT_ID)
        # Успешно
        return True

    def trade(self, event: {} = None):
        """ Учет покупки """
        if event:
            self.event = event
        # Проверим бота
        if self.event.peer_id != self.GAME_BOT_ID:
            return False
        # Пробьем регулярку
        tmp_match = self.regAccept.search(self.event.message)
        if not tmp_match:
            return False
        # Учет покупки
        tmp_count = int(tmp_match[1])
        tmp_name = tmp_match[2].lower()
        # Это мы не закупаем
        if not (tmp_name in self.items):
            return True
        # Уменьшим
        self.items[tmp_name].limit -= tmp_count
        self.log("  Куплен %s %s, осталось купить %s" % (tmp_count, tmp_name, self.items[tmp_name].limit))
        # Передадим гильдии если надо
        if self.config.storageMessage and self.items[tmp_name].guild:
            self.send("Передать %s - %s штук" % (tmp_name, tmp_count), self.config.storageChannel, self.config.storageMessage)
        # Успешно
        return True
