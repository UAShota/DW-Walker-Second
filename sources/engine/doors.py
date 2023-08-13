"""
Subclass for event doors
"""


class WalkerDoors:
    """ Answers for event doors"""

    def __init__(self, send: callable, register: callable, wait: callable, config: any):
        self.send = send
        self.wait = wait
        self.config = config
        self.baraban = [
            "лен",
            "железная руда",
            "бревно",
            "камень",
            # вторичка
            "каменный блок",
            "доска",
            "железный слиток",
            "ткань",
            # ресурсы
            "пещерный корень",
            "рыбий жир",
            "камнецвет",
            "необычный цветок",
            "адский гриб",
            "адский корень",
            "чистая первозданная вода",
            "болотник",
            "кровавый гриб",
            "сквернолист",
            "чернильник",
            "корень знаний",
            "сверкающая чешуя",
            "рыбий глаз",
            "необычная ракушка",
            "камень судьбы",
            "трофей победителя",
            # активные книги
            "грязный удар",
            "слабое исцеление",
            "удар вампира",
            "мощный удар",
            "сила теней",
            "расправа",
            "слепота",
            "рассечение",
            "берсеркер",
            "таран",
            "проклятие тьмы",
            "огонек надежды",
            "целебный огонь",
            "кровотечение",
            "заражение",
            "раскол",
            # пассивные книги
            "браконьер",
            "быстрое восстановление",
            "мародер",
            "внимательность",
            "инициативность",
            "исследователь",
            "ведьмак",
            "собиратель",
            "запасливость",
            "охотник за головами",
            "подвижность",
            "упорность",
            "регенерация",
            "расчетливость",
            "ошеломление",
            "рыбак",
            "неуязвимый",
            "колющий удар",
            "бесстрашие",
            "режущий удар",
            "феникс",
            "непоколебимый",
            "суеверность",
            "гладиатор",
            "воздаяние",
            "ученик",
            "прочность",
            "расторопность",
            "устрашение",
            "контратака",
            "дробящий удар",
            "защитная стойка",
            "стойка сосредоточения",
            "водохлеб",
            "картограф",
            "парирование",
            "ловкость рук",
            "презрение к боли",
            # кольца
            "кольцо великана",
            "кольцо гоблина",
            "кольцо зелий",
            "кольцо навыков",
            "кольцо экипировки",
            "кольцо редкостей",
            # зелья
            "зелье отравления",
            "зелье меткости",
            "зелье регенерации",
            "зелье характеристик",
            "зелье травм",
            "зелье снятия травм",
        ]
        register(self.doDoorAdms, r"перед которым расположены 4 рычага с именами Адмов")
        register(self.doDoorBottle, r"который отдается протяжным эхом: \"ВСЕ ИСПОЛЬЗУЮТ ЗЕЛЬЕ")
        register(self.doDoorColor, r"который отдается протяжным эхом: \"КАКОВ ЦВЕТ СЕРДЦА")
        register(self.doDoorElf, r"на крышке которого изображен тяжелораненый эльф")
        register(self.doDoorHeart, r"Где в настоящее время находится истинный спуск на путь к Сердцу Глубин")
        register(self.doDoorKings, r"Хтофтёмэд отфтпин")
        register(self.doDoorMap, r"Видимо, их нужно расставить по карте, чтобы сундук открылся")
        register(self.doDoorNames, r"На сундуке оставлены 3 практически стертых имени искателей приключений")
        register(self.doDoorQuit, r"какую из четырех Великих Рас никогда не примут в гильдию магов")
        register(self.doDoorRosa, r"В груди моей горел пожар, но сжег меня дотла")
        register(self.doDoorSarko, r"Сяэпьчео рущэр")
        register(self.doDoorStone, r"Видимо, этот камень нужно вложить в одну из вытянутых рук")
        register(self.doDoorWeapon, r"Докажи, что ты умеешь подбирать правильный подход к противнику")
        register(self.doDoorYear, r"Каждую плиту украшает символ, обозначающий конкретное время года")
        register(self.doEventDrum, r"^Судя по царапинам на полу")
        register(self.doEventPrison, "^Такими цепями, обычно, приковывают воров")
        register(self.doEventBook, r"^На алтаре покоится большая синяя книга")
        register(self.doEventBird, r"^Черный ворон с человеческим черепом")
        register(self.doEventSmithy, r"^Материалов здесь почти не осталось")
        register(self.doEventAltar, r"^Среди руин возвышается статуя одного")
        register(self.doEventGrid, r"^Путь туда, однако, перекрыт стальной решеткой")
        register(self.doEventShop, r"^В заброшенной лавке все еще остались ингредиенты")
        register(self.doEventTrain, r"^Ни вагонеток, ни чего-то подобного")
        register(self.doEventLight, r"^Сегодня он оказался каким-то особенно рассеянным")
        register(self.doEventTraktir, r"^Таких трактиров было много до времен")
        register(self.doEventSkeleton, r"^Уже готовясь к бою с ним, Вы услышали")
        register(self.doEventTown, r"^Низенькие многоэтажные дома практически")
        register(self.doEventYorik, r"^Черты черепа уже оплыли, но все еще")
        register(self.doEventRoots, r"^Однако, Вы оказались тут не одни")
        register(self.doEventOldman, r"Именно здесь живет старик, предлагающий")
        register(self.doEventWaterfall, r" Подъем ведет на вершину подземного водопада")
        register(self.doEventJail, r"Сложно оценить, сколько времени здесь находится")
        register(self.doEventFight, r"Вы оказались в смутно знакомой комнате")
        register(self.doEventPicklock, r"На массивной двери виднеется необычная")
        register(self.doEventManuscript, r"Почти все книги и манускрипты здесь уже")
        register(self.doEventSanctuary, r"Трудно сказать, кому именно принадлежало")
        register(self.doEventGhost, r"Попытавшись с ним поговорить, Вы лишь")
        register(self.doEventDust, r"Пыльные, но крепкие латы явно принадлежали")
        register(self.doEventTomb, r"Осмотрев открытый гроб, Вы нашли внутри")
        register(self.doEventFire, r"Судя по всему, костер оставил один из искателей")
        register(self.doEventShards, r"Рядом с костром Вы обнаруживаете почерневший")
        register(self.doEventChest, r"Сундук очень древний, украшенный разнообразными")
        register(self.doEventTrap, r"Больше всего это похоже на какую-то ловушку")

    def doDoorNames(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Гер")
            self.send("Натаниэль")
            self.send("Эмбер")

        self.wait(_match, sub)

    def doDoorKings(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Сокровище королей")

        self.wait(_match, sub)

    def doDoorMap(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Северо-восток")
            self.send("Северо-запад")
            self.send("Юг материка")

        self.wait(_match, sub)

    def doDoorQuit(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Уйти")

        self.wait(_match, sub)

    def doDoorAdms(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Грах")
            self.send("Ева")
            self.send("Трор")
            self.send("Смотритель")

        self.wait(_match, sub)

    def doDoorYear(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Осень")
            self.send("Зима")
            self.send("Весна")
            self.send("Лето")

        self.wait(_match, sub)

    def doDoorHeart(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Темнолесье")

        self.wait(_match, sub)

    def doDoorElf(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Пещерный корень")
            self.send("Первозданная вода")
            self.send("Рыбий жир")

        self.wait(_match, sub)

    def doDoorBottle(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send(str(self.config.memoryBottles))

        self.wait(_match, sub)

    def doDoorColor(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Фиолетовый")

        self.wait(_match, sub)

    def doDoorWeapon(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Разрезать мечом")
            self.send("Ударить молотом")
            self.send("Уколоть кинжалом")

        self.wait(_match, sub)

    def doDoorStone(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Человек")

        self.wait(_match, sub)

    def doDoorSarko(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Гробница веков")

        self.wait(_match, sub)

    def doDoorRosa(self, _match: []):
        """ Дверь """

        def sub():
            """ Delayed action """
            self.send("Роза")

        self.wait(_match, sub)

    def doEventDrum(self, _match: []):
        """ Бочки """
        self.send("Передвинуть бочки")

    def doEventPrison(self, _match: []):
        """ Пленник """
        self.send("Освободить")

    def doEventBook(self, _match: []):
        """ Книга """
        self.send("Взять книгу")

    def doEventBird(self, _match: []):
        """ Птица """
        self.send("Вспугнуть птицу")

    def doEventSmithy(self, _match: []):
        """ Кузня """
        self.send("Улучшить оружие")

    def doEventAltar(self, _match: []):
        """ Алтарь """
        self.send("Помолиться")

    def doEventGrid(self, _match: []):
        """ Решетка """
        self.send("Пройти мимо")

    def doEventShop(self, _match: []):
        """ Решетка """
        self.send("Камень судьбы")

    def doEventTrain(self, _match: []):
        """ Шла босиком не жалея ног """
        self.send("Идти вдоль дороги")

    def doEventLight(self, _match: []):
        """ Фонарь """
        self.send("Стащить его фонарь")

    def doEventTraktir(self, _match: []):
        """ Трактир """
        self.send("Обыскать зал")

    def doEventSkeleton(self, _match: []):
        """ Скелетоны """
        self.send("Атаковать")

    def doEventTown(self, _match: []):
        """ Поселение """
        self.send("Изучить поселение")

    def doEventYorik(self, _match: []):
        """ Поселение """
        self.send("Осторожно отойти")

    def doEventRoots(self, _match: []):
        """ Корешки """
        self.send("Корень знаний")

    def doEventOldman(self, _match: []):
        """ Дом """
        self.send("Забраться в дом")

    def doEventWaterfall(self, _match: []):
        """ Подъем ведет на вершину подземного водопада """
        self.send("Забраться")

    def doEventJail(self, _match: []):
        """ Сложно оценить, сколько времени здесь находится """
        self.send("Обыскать камеру")

    def doEventFight(self, _match: []):
        """ Вы оказались в смутно знакомой комнате """
        self.send("Атаковать")

    def doEventPicklock(self, _match: []):
        """ На массивной двери виднеется необычная """
        self.send("Взломать отмычкой")

    def doEventManuscript(self, _match: []):
        """ Почти все книги и манускрипты здесь уже """
        self.send("Осмотреть страницу")

    def doEventSanctuary(self, _match: []):
        """ Трудно сказать, кому именно принадлежало """
        self.send("Изучить святилище")

    def doEventGhost(self, _match: []):
        """ Попытавшись с ним поговорить, Вы лишь """
        self.send("Развоплотить духа")

    def doEventDust(self, _match: []):
        """ Пыльные, но крепкие латы явно принадлежали """
        self.send("Стереть пыль")

    def doEventTomb(self, _match: []):
        """ Осмотрев открытый гроб, Вы нашли внутри """
        self.send("Рассмотреть знаки")

    def doEventFire(self, _match: []):
        """ Судя по всему, костер оставил один из искателей """
        self.send("Забрать осколки")

    def doEventShards(self, _match: []):
        """ Рядом с костром Вы обнаруживаете почерневший """
        self.send("Забрать осколки")

    def doEventChest(self, _match: []):
        """ Сундук очень древний, украшенный разнообразными """
        self.send("Попытаться открыть силой")

    def doEventTrap(self, _match: []):
        """ Больше всего это похоже на какую-то ловушку """
        self.send("Подойти")
