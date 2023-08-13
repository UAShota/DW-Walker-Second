"""
Walker configuration
"""

from sources.engine.classes import WalkerFight

from .loader_config import *


class WalkerConfig(LoaderConfig):
    """ Класс настроек """

    def __init__(self):
        """ Общие параметры """
        super().__init__()
        # Токен ВК
        self.token = ""
        # Ключ API
        self.api = ""
        # Цвет консоли
        self.color = 92
        # Мсек ожидания перед отправкой мин
        self.waitMin = 2000
        # Мсек ожидания перед отправкой макс
        self.waitMax = 4000
        # Алерт на продавца товаров (0 - уйти, 1 - купить, 2 - алерт)
        self.trader = 0
        # Процент здоровья для отдыха у костра
        self.restHp = 35
        # Количество травм идти домой
        self.injuriesForHome = 10
        # Количество травм сидеть в фонтане
        self.injuriesForFountain = 8
        # Алерт если маскировки меньше чем задано
        self.cloakLow = 2
        # Алерт если рюкзака меньше чем задано
        self.inventoryLow = 5
        # Сколько выпито бутылок памяти
        self.memoryBottles = 4
        # Сдача трофеев
        self.trophLimit = 500
        # Охотится ли на оленей (0 - нет, 1 - да)
        self.hunting = 0
        # Разбирать завалы / нырять (0 - нет, 1 - да)
        self.working = 1
        # Искать лут в пещере (0 - нет, 1 - да)
        self.searching = 1
        # Проходить лабиринты (0 - нет, 1 - да)
        self.labirint = 1
        # Что делать с элитками (0 - уведомлять, 1 - драться)
        self.eliteChoice = 1
        # Собирать адские ресурсы (0 - нет, 1 - да)
        self.gatherHell = 0
        # Кидать кубики (0 - нет, 1 - да)
        self.rollDice = 0
        # Спускаться вниз автоматически (0 - нет, 1 - да)
        self.goDown = 0
        # Процент голода для перекуса
        self.honger = 35
        # Час для ухода в таверну (None - не уходить)
        self.sleepHour = 2
        # Принимать пвп
        self.warrior = False
        # Что качать на кухне (силы, ловкости, выносливости, None)
        self.constat = "выносливости"

    def battle(self, actions: dict, send: any, fight: WalkerFight):
        """ Логика боя """
        tmp_power_punch = '|Слабое исцеление|' in actions
        tmp_blind = '|Сила теней|' in actions
        tmp_crush = '|Раскол|' in actions
        tmp_attack = 'Атака' in actions
        tmp_shield = 'Блок щитом' in actions and fight.isStand
        tmp_bottle = False and 'Зелье' in actions and fight.isStand and fight.myBag
        tmp_light = "Яркий свет" in actions and fight.isStand
        tmp_stcrush = "#Дробящий"
        tmp_stcut = "#Режущий"
        tmp_stchop = "#Рубящий"

        if fight.isInit and fight.myConcentration == 5:
            return send("Сбежать")

        elif fight.enemyAttack > 2000 and tmp_shield:
            return send("Блок щитом")

        elif fight.myPercent < 50 and tmp_bottle:
            return send("Зелье")

        elif tmp_power_punch and fight.myPercent < 70:
            return send("|Слабое исцеление|")

        elif tmp_power_punch and fight.enemyPercent < 30:
            return send("|Слабое исцеление|")

        elif fight.myPercent < 70 and fight.isElite and tmp_bottle:
            return send("Зелье")

        elif fight.enemyPercent < 50 and tmp_shield:
            return send("Блок щитом")

        elif fight.myPercent < 70 and tmp_shield:
            return send("Блок щитом")

        #elif fight.isInit and fight.isStand and fight.enemyArmor > 40 and fight.myStand != tmp_stcrush:
        #    send(fight.myStand)
        #    fight.myStand = tmp_stcrush
        #    return True

        #elif fight.isStand and fight.enemyArmor >= 50 and fight.myStand != tmp_stcrush:
        #    send(fight.myStand)
        #    fight.myStand = tmp_stcrush
        #    return True

        #elif fight.isInit and fight.isStand and fight.myAccuracy == 95 and fight.myStand == tmp_stcut and fight.enemySize > 130:
        #    send(fight.myStand)
        #    fight.myStand = tmp_stchop
        #    return True

        #elif fight.isStand and fight.myAccuracy < 90 and fight.myStand != tmp_stcut and fight.enemyArmor < 50:
        #    send(fight.myStand)
        #    fight.myStand = tmp_stcut
        #    return True

        elif fight.enemyPercent < 70 and tmp_light:
            return send("Яркий свет")

        elif tmp_blind:
            return send("|Сила теней|")

        elif tmp_crush:
            return send("|Раскол|")

        elif tmp_attack:
            return send("Атака")

        else:
            return False

    def bottle(self, actions: {}, send: any):
        """ Логика бутылок """

        tmp_super_heal = "Идеальное зелье" in actions
        tmp_yeah_heal = "Чудесное зелье" in actions
        tmp_max_heal = "Сильное зелье" in actions
        tmp_big_heal = "Большое зелье" in actions
        tmp_magic_heal = "Обычное зелье" in actions
        tmp_power_heal = "Простое зелье" in actions
        tmp_low_heal = "Слабое зелье" in actions

        if tmp_super_heal:
            return send("Идеальное зелье")
        if tmp_yeah_heal:
            return send("Чудесное зелье")
        elif tmp_max_heal:
            return send("Сильное зелье")
        elif tmp_big_heal:
            return send("Большое зелье")
        elif tmp_magic_heal:
            return send("Обычное зелье")
        elif tmp_power_heal:
            return send("Простое зелье")
        elif tmp_low_heal:
            return send("Слабое зелье")
        else:
            return False

    def seller(self, register):
        """ Логика автопродажи """
        register("14436", "Пещ. корень", 1)
        register("14453", "Рыбий жир", 0)
        register("14452", "Необ. цветок", 0)
        register("14438", "Камнецвет", 0)
        register("14440", "Болотник", 0)
        register("14441", "Сквернолист", 0)
        register("14628", "Адский кор.", 0)
        register("14627", "Адский гриб", 0)
        register("14470", "Сверк. чешуя", 0)
        register("14472", "Рыбий глаз", 0)
        register("14550", "Ракушка", 1)
        register("14608", "трофей победителя", 0)
        # Оружие
        register("13702", "+2 Тяж. ветка", 1)
        register("13736", "+4 Слом. меч", 1)
        register("13739", "+6 Ржав. кинжал", 1)
        #register("13741", "+8 Ржавый меч", 1)
        register("13743", "+10 Тупой топор.", 1)
        #register("13745", "+12 Кост. нож", 1)
        register("13747", "+14 Топор дров.", 1)
        register("13749", "+16 Копье охот.", 1)
        register("13751", "+18 Жел. кинж.", 1)
        #register("13753", "+20 Корот. меч", 1)
        register("13755", "+22 Копье стр.", 1)
        register("13757", "+24 Полут. меч", 1)
        register("13759", "+26 Тяж. булава", 1)
        register("13761", "+28 Боев. молот", 1)
        register("13763", "+30 Двуруч. меч", 1)
        register("13765", "+32 Цер. кинжал", 1)
        register("13767", "+34 Тум. клинок", 1)
        register("13769", "+36 Топор берс.", 1)
        register("13771", "+38 Б. трезубец", 1)
        register("13773", "+40 Сабля прин.", 1)
        register("13775", "+42 Кор. стилет", 1)
        register("13777", "+44 Копье ОНД", 1)
        register("13779", "+46 Молот гром.", 1)
        register("13781", "+48 Булава КЧ", 1)
        register("13783", "+50 Украш. меч", 1)
        register("13785", "+52 Кинжал ПС", 1)
        register("13787", "+54 Приз. бурю", 1)
        register("13789", "+56 Сверк. смер.", 1)
        register("13791", "+58 Темн. течен.", 1)
        register("13793", "+60 Повел. стих.", 1)
        # Броня
        register("13795", "+1 Дыр. накидка", 1)
        register("13798", "+2 Пот. рубаха", 1)
        #register("13800", "+3 Стар. жилет", 1)
        #register("13802", "+4 Ржав. кольч.", 1)
        #register("13804", "+5 Раск. кираса", 1)
        register("13806", "+6 Кож. туника", 1)
        register("13808", "+7 Тяж. шуба", 1)
        register("13810", "+8 Стег. доспех", 1)
        register("13812", "+9 Клеп. броня", 1)
        register("13814", "+10 Легк. кольч.", 1)
        register("13816", "+11 Чеш. доспех", 1)
        register("13818", "+12 Наб. доспех", 1)
        register("13820", "+13 Проч. кир.", 1)
        register("13822", "+14 Полулаты", 1)
        register("13824", "+15 Полн. лат.", 1)
        register("13826", "+16 Рыц. комп.", 1)
        register("13828", "+17 Рыц. латы", 1)
        register("13830", "+18 Миф. кольч.", 1)
        register("13832", "+19 Гном. досп.", 1)
        register("13834", "+20 Кор. латы", 1)
        register("13836", "+21 Брон. мант.", 1)
        register("13838", "+22 Броня ОНД", 1)
        register("13840", "+23 Досп. гром.", 1)
        register("13842", "+24 Доспех КЧ", 1)
        register("13844", "+25 Украш. досп.", 1)
        register("13846", "+26 Латы ПЦ", 1)
        register("13848", "+27 Латы УН", 1)
        register("13850", "+28 Доспехи СД", 1)
        register("13852", "+29 Доспехи ВП", 1)
        register("13854", "+30 Страж. стих.", 1)
        # Факелы
        register("14052", "+1 Горящ. ветка", 1)
        register("14054", "+2 Прост. факел", 1)
        register("14056", "+3 Укреп. факел", 1)
        register("14058", "+4 Гном. факел", 1)
        register("14060", "+5 Волш. факел", 1)
        register("14062", "+6 Факел героя", 1)
        register("14064", "+7 Вечн. факел", 1)
        # Щиты
        #register("14556", "+1 Кусок табур.", 1)
        #register("14558", "+2 Круг. щит", 1)
        #register("14560", "+3 Укреп. щит", 1)
        #register("14562", "+4 Гном. щит", 1)
        #register("14564", "+5 Рыц. щит", 1)
        #register("14566", "+6 Тяж. щит", 1)
        #register("14568", "+7 Баш. щит", 1)
        # Перчатки
        #register("14905", "+1 Льнян. перч.", 1)
        #register("14907", "+2 Ткан. рукав.", 1)
        register("14909", "+3 Кож. обмот.", 1)
        register("14911", "+4 Кож. перч.", 1)
        register("14913", "+5 Укреп. перч.", 1)
        register("14915", "+6 Латн. рук.", 1)
        register("14917", "+7 Рыц. перч.", 1)
        # Пояса
        #register("14030", "+1 Верев. пояс", 1)
        #register("14032", "+2 Ткан. пояс", 1)
        register("14034", "+3 Кожан. пояс", 1)
        register("14036", "+4 Кольч. пояс", 1)
        register("14038", "+5 Украш. пояс", 1)
        register("14040", "+6 Мифр. пояс", 1)
        register("14042", "+7 Кор. пояс", 1)
        # Сапоги
        #register("14854", "+1 Стар. сапоги", 1)
        #register("14856", "+2 Прост. бот.", 1)
        register("14858", "+3 Кож. сапоги", 1)
        register("14860", "+4 Укреп. сап.", 1)
        register("14862", "+5 Кольч. сап.", 1)
        register("14864", "+6 Мех. сапоги", 1)
        register("14866", "+7 Рыц. сапоги", 1)
        # Амулеты
        #register("13856", "+1 Бронзовый", 1)
        #register("13859", "+2 С листьями", 1)
        register("13861", "+3 С изумруд.", 1)
        register("13863", "+4 Темный", 1)
        register("13865", "+5 Золотой", 1)
        register("13867", "+6 С черепом", 1)
        register("13869", "+7 С жемчугом", 1)
        # Кольца
        #register("14238", "Кол. зелий", 1)
        #register("14316", "Кол. гоблина", 1)
        register("14318", "Кол. великана", 1)
        register("14240", "Кол. навыков", 1)
        register("14242", "Кол. экип.", 1)
        register("14244", "Кол. редкост.", 1)
        # Посохи
        register("14995", "Железный прут", 1)
        register("14997", "Посох когтя", 1)
        register("14999", "Жемчужный посох", 1)
        register("15001", "Кристаллический посох", 1)
        register("15003", "Морозный посох", 1)
        register("15005", "Посох инквизитора", 1)

    def transfer(self, register):
        """ Логика автопередачи """
        register('13580', 'Грязный удар', 1)
        register('13581', 'Слабое исцеление', 1)
        register('13582', 'Удар вампира', 1)
        register('13583', 'Мощный удар', 1)
        register('13592', 'Сила теней', 1)
        register('13595', 'Расправа', 1)
        register('13600', 'Слепота', 1)
        register('13603', 'Рассечение', 1)
        register('13606', 'Берсеркер', 1)
        register('13609', 'Таран', 1)
        register('13612', 'Проклятие тьмы', 1)
        register('13615', 'Огонек надежды', 1)
        register('13619', 'Целебный огонь', 1)
        register('13623', 'Кровотечение', 1)
        register('13626', 'Заражение', 1)
        register('13628', 'Раскол', 1)
        register('13639', 'Быстрое восстановление', 1)
        register('13642', 'Мародер', 1)
        register('13644', 'Внимательность', 1)
        register('13646', 'Инициативность', 1)
        register('13648', 'Исследователь', 1)
        register('13650', 'Ведьмак', 1)
        register('13652', 'Собиратель', 1)
        register('13654', 'Запасливость', 1)
        register('13656', 'Охотник за головами', 1)
        register('13658', 'Подвижность', 1)
        register('13660', 'Упорность', 1)
        register('13662', 'Регенерация', 1)
        register('13664', 'Расчетливость', 1)
        register('13666', 'Презрение к боли', 1)
        register('13670', 'Рыбак', 1)
        register('13672', 'Неуязвимый', 1)
        register('13674', 'Колющий удар', 1)
        register('13677', 'Бесстрашие', 1)
        register('13679', 'Режущий удар', 1)
        register('13681', 'Феникс', 1)
        register('13683', 'Непоколебимый', 1)
        register('13685', 'Суеверность', 1)
        register('13687', 'Гладиатор', 1)
        register('13689', 'Воздаяние', 1)
        register('13691', 'Ученик', 1)
        register('13693', 'Прочность', 1)
        register('13695', 'Расторопность', 1)
        register('13697', 'Устрашение', 1)
        register('13699', 'Контратака', 1)
        register('14505', 'Дробящий удар', 1)
        register('14507', 'Защитная стойка', 1)
        register('14777', 'Стойка сосредоточения', 1)
        register('14779', 'Водохлеб', 0)
        register('14970', 'Картограф', 0)
        register('14972', 'Браконьер', 0)
        register('14793', 'Бревно', 0)
        register('14794', 'Камень', 0)
        register('14795', 'Желез. руда', 0)
        register('14796', 'Лен', 0)
        register('14797', 'Доска', 0)
        register('14798', 'Каменный блок', 0)
        register('14799', 'Железный слиток', 0)
        register('14800', 'Ткань', 0)
        register('14660', 'Карта озера', 0)
        register('14661', 'Карта сокровищ', 0)
        register('14662', 'Карта угодий', 0)
        register('14663', 'Карта источника', 0)
        register('14664', 'Карта испытаний', 0)
        register('14665', 'Карта окрестностей', 0)
        register('14963', 'Карта руин', 0)
