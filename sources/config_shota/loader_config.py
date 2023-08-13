"""
Base configuration
"""


class LoaderConfig:
    """ Класс общих настроек """

    def __init__(self):
        """ Общие параметры """

        # Номер чата с гильдейским складом (None)
        self.storageChannel = 2000000014
        # Номер чата с гильдейским складом (None)
        self.storageMessage = 675644
        # ID ВК алерта (Номер, None)
        self.selfID = 384297286
        # ID ВК алерта (Номер, None)
        self.alertID = 384297286
        # Сообщения Windows
        self.alertToast = True
        # Файл алерта (Путь, None)
        self.alertFile = "sources/sounds/alert_1.mp3"
        # Временная зона
        self.utc = +3
        # Цвет консоли
        self.color = 94
