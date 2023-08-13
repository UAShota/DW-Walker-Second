"""
Trader configuration
"""

from .loader_config import *


class TraderConfig(LoaderConfig):
    """ Класс торговых настроек """

    def __init__(self, register):
        """ Общие параметры """
        super().__init__()
        # Токен ВК
        self.token = ""
        # Цвет консоли
        self.color = 33
        # Идентификатор сообщения в гильдейском чате для передачи лута (None)
        self.storageMessage = None
        # первичка
        register("лен", 1500, 50, False)
        register("железная руда", 1500, 50, False)
        register("бревно", 300, 50, False)
        register("камень", 300, 50, False)
        # вторичка
        register("каменный блок", 1200, 50, False)
        register("доска", 1200, 50, False)
        register("железный слиток", 4500, 50, False)
        register("ткань", 4500, 50, False)
        # ресурсы
        register("пещерный корень", 50, 50, True)
        register("рыбий жир", 50, 50, True)
        register("камнецвет", 50, 50, True)
        register("адский гриб", 50, 50, True)
        register("адский корень", 50, 50, True)
        register("чистая первозданная вода", 50, 50, True)
        register("болотник", 50, 50, True)
        register("кровавый гриб", 1000, 50, True)
        register("сквернолист", 50, 50, True)
        register("чернильник", 6800, 50, True)
        register("корень знаний", 1500, 50, True)
        register("сверкающая чешуя", 50, 50, True)
        register("рыбий глаз", 50, 50, False)
        register("ракушка", 1000, 50, False)
        # активные книги
        register("грязный удар", 2500, 50, True)
        register("слабое исцеление", 1000, 50, True)
        register("удар вампира", 4000, 50, True)
        register("мощный удар", 4000, 50, True)
        register("сила теней", 2000, 50, True)
        register("расправа", 3000, 50, True)
        register("слепота", 4000, 50, True)
        register("рассечение", 4000, 50, True)
        register("берсеркер", 2000, 50, True)
        register("таран", 2000, 50, True)
        register("проклятие тьмы", 1000, 50, True)
        register("огонек надежды", 1000, 50, True)
        register("целебный огонь", 4000, 50, True)
        register("кровотечение", 2000, 50, True)
        register("заражение", 1000, 50, True)
        register("раскол", 4000, 50, True)
        # пассивные книги
        register("быстрое восстановление", 150, 50, True)
        register("мародер", 4000, 50, True)
        register("внимательность", 1500, 50, True)
        register("инициативность", 4000, 50, True)
        register("исследователь", 500, 50, True)
        register("ведьмак", 2500, 50, True)
        register("собиратель", 2000, 50, True)
        register("запасливость", 1500, 50, True)
        register("охотник за головами", 3000, 50, True)
        register("подвижность", 4000, 50, True)
        register("упорность", 400, 50, True)
        register("регенерация", 4000, 50, True)
        register("расчетливость", 1500, 50, True)
        register("презрение к боли", 1000, 50, True)
        register("ошеломление", 4000, 50, True)
        register("рыбак", 3000, 50, True)
        register("неуязвимый", 2000, 50, True)
        register("колющий удар", 1000, 50, True)
        register("бесстрашие", 400, 50, True)
        register("режущий удар", 1000, 50, True)
        register("феникс", 3000, 50, True)
        register("непоколебимый", 4000, 50, True)
        register("суеверность", 2000, 50, True)
        register("гладиатор", 4000, 50, True)
        register("воздаяние", 4000, 50, True)
        register("ученик", 4000, 50, True)
        register("прочность", 1000, 50, True)
        register("расторопность", 500, 50, True)
        register("устрашение", 500, 50, True)
        register("контратака", 4000, 50, True)
        register("колющий удар", 1000, 50, True)
        register("дробящий удар", 1500, 50, True)
        register("защитная стойка", 400, 50, True)
        register("стойка сосредоточения", 1000, 50, True)
        register("водохлеб", 1000, 50, True)
        register("картограф", 4000, 50, True)
        register("браконер", 1000, 50, True)
        # Адмы
        register("свиток заточки", 10000, 50, True)
        register("обломок сердца", 10000, 50, True)
        register("цветок адмов", 20000, 50, True)
        register("жемчужина адмов", 20000, 50, True)
        register("кровь адмов", 20000, 50, True)
        # Кольца
        register("малое кольцо силы", 10000, 50, True)
        register("малое кольцо ловкости", 10000, 50, True)
        register("малое кольцо выносливости", 10000, 50, True)
        register("малое кольцо концентрации", 10000, 50, True)
        register("кольцо заточки", 10000, 50, True)
        register("кольцо S ранга", 10000, 50, True)
