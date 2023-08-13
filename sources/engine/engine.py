"""
Base bot engine
"""

import ctypes
import logging
import os
import platform
import re
import threading
import time
from datetime import timedelta
from threading import Thread

import colorama

from ..vkapi import *
from ..vkapi.longpoll import *

# Импортируем платформозависимость
if platform.system().lower().startswith("win"):
    from win10toast import ToastNotifier

    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    import pygame


class Engine:
    """ Движок методов """

    # Каталог логов
    __ENGINE_VERSION__ = 2.16

    # Каталог логов
    __LOG_DIR__ = "logs/"

    def __init__(self, config: any, name: str, lock: object = None, token: str = "", color: int = 0):
        """ Конструктор """
        self.name = name
        self.config = config
        self.session = None
        self.longpoll = None
        self.logger = None
        self.event = None
        self.channel = 0
        self.ts = 0
        self.rules = []
        self.win = platform.system().lower().startswith("win")
        # Перегрузка лока
        if lock:
            self.lock = lock
        else:
            self.lock = threading.Lock()
        # Перегрузка токена
        if token:
            self.token = token
        else:
            self.token = config.token
        # Перегрузка цвета
        if color:
            self.color = color
        else:
            self.color = config.color
        # Загрузка модулей
        self.load()

    def connected(self):
        """ Событие подключения """
        return

    def reconnect(self):
        """ Переподключение """
        self.session = VkApi(token=self.token)
        self.longpoll = VkLongPoll(self.session)
        if self.ts > 0:
            self.longpoll.ts = self.ts
        self.connected()
        self.log("Connected")

    def load(self):
        """ Вспомогательные модули """
        # Цвета
        colorama.init()
        # Звук
        if self.win:
            pygame.init()
        # Логер
        if not os.path.isdir(self.__LOG_DIR__):
            os.mkdir(self.__LOG_DIR__)
        # Самолог
        self.logger = logging.getLogger(str(self.name))
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.FileHandler("%s%s.log" % (self.__LOG_DIR__, self.name), "w", "utf-8"))
        # Запустимся
        self.log("Engine v%s" % self.__ENGINE_VERSION__)

    def log(self, text: str, console: bool = True, level: int = 0):
        """ Логирование """
        self.lock.acquire()
        try:
            text = "%s [%s] %s " % (
                self.toUTC(datetime.today()).strftime("%H:%M:%S"), self.name, text.replace("\n", " "))
            # В консоль только важное
            if console:
                if level > 0:
                    tmp_color = 91
                else:
                    tmp_color = self.color
                print(("\033[%sm%s" % (tmp_color, text))[:85])
            # В лог - все
            if level == 1:
                self.logger.error(text)
            elif level == 2:
                self.logger.exception(text)
            else:
                self.logger.info(text)
        finally:
            self.lock.release()
        return

    def alert(self, text: str, level: int = 1):
        """ Уведомление о критическом действии """
        self.log(text, level=level)
        # Звук
        if self.win and self.config.alertFile:
            try:
                pygame.mixer.Sound(self.config.alertFile).play()
            except Exception as E:
                print(E.args)
                pass
        # Тостер
        if self.win and self.config.alertToast:
            try:
                ToastNotifier().show_toast("Alarma!", text)
            except Exception as E:
                print(E.args)
                pass
        # В личку
        if self.config.alertID:
            try:
                self.send(text, self.config.alertID)
            except Exception as E:
                print(E.args)
                pass
        # Пока все
        return

    def catch(self, text: str, e: Exception, crit: bool):
        """ Уведомление о исключении """
        tmp_error = "%s %s" % (text, repr(e))
        # Определим тип
        if crit:
            self.alert(tmp_error, 2)
        else:
            self.log(tmp_error, level=2)
        # Подождем
        self.sleep(30, "exception")

    def method(self, name: str, params: {}):
        """ Отправка метода """
        while True:
            try:
                return self.session.method(name, params)
            except Exception as e:
                self.catch("%s send failed, retry..." % self.__class__.__name__, e, False)
                pass

    def mark(self, event: Event, readed: bool = True):
        """ Уведомление о прочтении """
        tmp_params = {
            "peer_id": event.peer_id,
            "start_message_id": event.message_id,
            "mark_conversation_as_read": readed,
        }
        # Отправим
        return self.method("messages.markAsRead", tmp_params)

    def send(self, text: str, channel: int = 0, reply: int = 0, forward: int = 0, payload: str = ""):
        """ Отправка сообщения """
        self.log("> " + text)
        # Куда писать
        if channel:
            tmp_channel = channel
        else:
            tmp_channel = self.channel
        # Заполним
        tmp_params = {
            "peer_id": tmp_channel,
            "message": text,
            "random_id": 0,
        }
        # Нагрузка
        if payload:
            tmp_params["payload"] = payload
        # Если надо ответить
        if reply:
            tmp_params["reply_to"] = reply
        # Если надо переслать
        if forward:
            tmp_params["forward_messages"] = forward
        # Отправим
        return self.method("messages.send", tmp_params)

    def delete(self, messagesids: int):
        """ Удаление сообщения """
        tmp_params = {
            "message_ids": messagesids,
            "delete_for_all": 1
        }
        # Отправим
        return self.method("messages.delete", tmp_params)

    def getphoto(self, channel: int, message: int, size: int, media: str = "photo"):
        """ Получение фото """
        self.log("> ищу фото для %s" % message)
        tmp_params = {
            "peer_id": channel,
            "media_type": media,
            "start_from": message,
            "count": 1
        }
        # Отправим
        tmp_data = self.method("messages.getHistoryAttachments", tmp_params)
        # Найдем нужную ссылку
        for tmp_photo in tmp_data["items"][0]["attachment"][media]["sizes"]:
            if tmp_photo["height"] == size:
                self.log("Найдено как %s" % tmp_photo["url"])
                return tmp_photo["url"]
        # Не найдено
        self.log("Не найдено " + str(tmp_data))
        return None

    def sleep(self, val: int, log: str):
        """ Ожидание с уведомлением """
        self.log("* ожидаем %s сек для %s" % (val, log), False)
        time.sleep(val)

    def compile(self, pattern: str):
        """ Сборка регулярки """
        return re.compile(pattern, re.IGNORECASE | re.UNICODE | re.DOTALL | re.MULTILINE)

    def toUTC(self, value: datetime):
        """ Перевод времени """
        return value + timedelta(hours=self.config.utc)

    def toInt(self, val: str):
        """ Безопасный str to int """
        if val:
            return int(val)
        else:
            return 0

    def caption(self, text: str, log: bool = False):
        """ Текст окна """
        if self.win:
            ctypes.windll.kernel32.SetConsoleTitleW(text)
        if log:
            self.log(text)

    def addrule(self, callback: object, pattern: str):
        """ Регистрация правила """
        self.rules.append([callback, self.compile(pattern)])

    def work(self, log: bool):
        """ Обработка выражения """
        try:
            for tmp_op, tmp_reg in self.rules:
                tmp_match = tmp_reg.search(self.event.message)
                if not tmp_match:
                    continue
                if log:
                    self.log(self.event.message)
                # Выполним
                return tmp_op(tmp_match) or tmp_match
        except Exception as e:
            self.catch("%s handled exception" % self.__class__.__name__, e, True)
            pass
        # Ничего не найдено
        return False

    def read(self):
        """ Чтение пакетов """
        while True:
            try:
                # Переподключимся
                if not self.session:
                    self.reconnect()
                # Перебираем события
                for tmpEvent in self.longpoll.check():
                    if tmpEvent.type == VkEventType.MESSAGE_NEW:
                        yield tmpEvent
                # Сохраним TS
                self.ts = self.longpoll.ts
            except Exception as e:
                self.catch("%s longpoll exception" % self.__class__.__name__, e, False)
                self.session = None
                pass

    def threadread(self, callback: callable):
        """ Жизненный цикл """
        for self.event in self.read():
            try:
                callback()
            except Exception as e:
                self.catch("%s thread exception" % self.__class__.__name__, e, True)
                pass
        return

    def thread(self, callback: callable):
        """ Запусе жизненного цикла """
        Thread(target=self.threadread, args=(callback,)).start()
