"""
    Subclass for books
"""

class WalkerBooks:
    """ Answers for event books"""

    def __init__(self, send: callable, register: callable):
        self.send = send
        register(self.doBookAttentiv, r"не только следить за всем, происходящим вокруг")
        register(self.doBookBerserker, r"кровь, заливающая глаза, придаст")
        register(self.doBookBleeding, r"не столько длина пореза, сколько его")
        register(self.doBookConcentration, r"отрешившись от внешнего мира, однако")
        register(self.doBookBlind, r"грязь под ногами, как самый простой вариант")
        register(self.doBookBigPunch, r"всю накопленную за это время силу высвободить")
        register(self.doBookFastRecovery, r"поможет сэкономить время при перевязке")
        register(self.doBookCollector, r"не всегда ценность находки может быть")
        register(self.doBookCounter, r"если провести удар прямо в этот момент")
        register(self.doBookCrushing, r"более важен размах, который усилит тяжесть")
        register(self.doBookDarkSize, r"убедиться, что вокруг нет ни единого источника")
        register(self.doBookDirtyPunch, r"только в неожиданный момент, свободной")
        register(self.doBookDefense, r"Переждав несколько ударов, можно восстановить")
        register(self.doBookExplorer, r"не обязательно настроены агрессивно")
        register(self.doBookImmune, r"не подставляя свои слабые точки под")
        register(self.doBookIniciative, r"даже, казалось бы, всего одно умение")
        register(self.doBookInfection, r"проникает в саму кровь врага, отравляя")
        register(self.doBookFearless, r"следить за каждым движением, которое")
        register(self.doBookFisher, r"обитают ближе ко дну, чаще скрываясь")
        register(self.doBookGladiator, r"эти бойцы не носили, однако это позволяло")
        register(self.doBookHamster, r"если связывать их в одну охапку")
        register(self.doBookHeadHunter, r"выследить их можно по особым")
        register(self.doBookHealFire, r"но не стоит страшиться - ведь Вам")
        register(self.doBookHonor, r"падал, но снова вставал, продолжая")
        register(self.doBookHopeFire, r"использовать собственный факел даже")
        register(self.doBookJuggle, r"выверенные движения позволят снять пробку")
        register(self.doBookLearner, r"впитывать знания в любой ситуации")
        register(self.doBookMaroder, r"не брезговать осмотреть каждый карман")
        register(self.doBookMaps, r"зарисовать на бумаге, каждый поворот")
        register(self.doBookMobility, r"своевременно и быстро совершенное")
        register(self.doBookNightmare, r"самое эффективное из них, позволяющее ослабить")
        register(self.doBookParry, r"нужный момент подставить свой клинок под удар")
        register(self.doBookPierce, r"прямой удар острием вперед")
        register(self.doBookPhoenix, r"переродиться из пепла, но только в том случае")
        register(self.doBookPoacher, r"разрезать вдоль, аккуратно поддев ножом")
        register(self.doBookPunish, r"будет достигнут только если противник")
        register(self.doBookPrudence, r"точно соблюдать время между ними, и тогда")
        register(self.doBookRegen, r"если они небольшие - затянутся сами собой")
        register(self.doBookReply, r"истинный путь, в зависимости от совершенных")
        register(self.doBookScare, r"такую позу, которая максимально подчеркнет")
        register(self.doBookSecha, r"резким взмахом, едва задевая самым")
        register(self.doBookSlash, r"нанести удар вдоль, максимально сблизившись")
        register(self.doBookSmallHeal, r"жизненные силы вокруг себя и направить")
        register(self.doBookSpeed, r"позволит быстрее перетаскивать камни")
        register(self.doBookSplit, r"в сочленение между пластинами")
        register(self.doBookStun, r"резкий и громкий звук, который")
        register(self.doBookSupersition, r"пусть эти приметы и не всегда будут полезны")
        register(self.doBookTaran, r"дополнительный вес, придающий силу")
        register(self.doBookUnstoppable, r"очистить разум от посторонних мыслей")
        register(self.doBookUnbreakable, r"использовать особые пластины в доспехе")
        register(self.doBookVamp, r"вонзить в плоть, незащищенную броней")
        register(self.doBookWater, r"позволит быстро откупорить крышку")
        register(self.doBookWicher, r"спасительной жидкостью, которая, иногда")

    def doBookDirtyPunch(self, _match: []):
        """ Книга грязного удара """
        self.send("Грязный удар")

    def doBookDefense(self, _match: []):
        """ Книга защитной стойки """
        self.send("Защитная стойка")

    def doBookExplorer(self, _match: []):
        """ Книга исследователя """
        self.send("Исследователь")

    def doBookImmune(self, _match: []):
        """ Книга неуязвимости """
        self.send("Неуязвимый")

    def doBookIniciative(self, _match: []):
        """ Книга инициативы """
        self.send("Инициативность")

    def doBookInfection(self, _match: []):
        """ Книга заражения """
        self.send("Заражение")

    def doBookFearless(self, _match: []):
        """ Книга бесстрашия """
        self.send("Бесстрашие")

    def doBookFisher(self, _match: []):
        """ Книга рыбака """
        self.send("Рыбак")

    def doBookHamster(self, _match: []):
        """ Книга запасливости """
        self.send("Запасливость")

    def doBookHeadHunter(self, _match: []):
        """ Книга охотника за головами """
        self.send("Охотник за головами")

    def doBookHealFire(self, _match: []):
        """ Книга целебного огня """
        self.send("Целебный огонь")

    def doBookHonor(self, _match: []):
        """ Книга упорности """
        self.send("Упорность")

    def doBookHopeFire(self, _match: []):
        """ Книга огонька надежды """
        self.send("Огонек надежды")

    def doBookJuggle(self, _match: []):
        """ Книга ловкости рук """
        self.send("Ловкость рук")

    def doBookLearner(self, _match: []):
        """ Книга ученика """
        self.send("Ученик")

    def doBookGladiator(self, _match: []):
        """ Книга гладиатора """
        self.send("Гладиатор")

    def doBookAttentiv(self, _match: []):
        """ Книга внимательности """
        self.send("Внимательность")

    def doBookBerserker(self, _match: []):
        """ Книга берсеркера """
        self.send("Берсеркер")

    def doBookBleeding(self, _match: []):
        """ Книга кровотечения """
        self.send("Кровотечение")

    def doBookConcentration(self, _match: []):
        """ Книга стойки сосредоточения """
        self.send("Стойка сосредоточения")

    def doBookSecha(self, _match: []):
        """ Книга рассечения """
        self.send("Рассечение")

    def doBookBlind(self, _match: []):
        """ Книга слепоты """
        self.send("Слепота")

    def doBookBigPunch(self, _match: []):
        """ Книга мощного удара """
        self.send("Мощный удар")

    def doBookFastRecovery(self, _match: []):
        """ Книга быстрого восстановления """
        self.send("Быстрое восстановление")

    def doBookCollector(self, _match: []):
        """ Книга собирателя """
        self.send("Собиратель")

    def doBookCounter(self, _match: []):
        """ Книга контратаки """
        self.send("Контратака")

    def doBookCrushing(self, _match: []):
        """ Книга дробящего удара """
        self.send("Дробящий удар")

    def doBookDarkSize(self, _match: []):
        """ Книга сил тьмы """
        self.send("Сила теней")

    def doBookUnstoppable(self, _match: []):
        """ Книга непоколебимости """
        self.send("Непоколебимый")

    def doBookUnbreakable(self, _match: []):
        """ Книга прочности """
        self.send("Прочность")

    def doBookVamp(self, _match: []):
        """ Книга вампира """
        self.send("Удар вампира")

    def doBookWater(self, _match: []):
        """ Книга водохлеба """
        self.send("Водохлеб")

    def doBookWicher(self, _match: []):
        """ Книга ведьмака """
        self.send("Ведьмак")

    def doBookNightmare(self, _match: []):
        """ Книга проклятия тьмы """
        self.send("Проклятие тьмы")

    def doBookParry(self, _match: []):
        """ Книга парирования """
        self.send("Парирование")

    def doBookPierce(self, _match: []):
        """ Книга колющего удара """
        self.send("Колющий удар")

    def doBookPhoenix(self, _match: []):
        """ Книга феникса """
        self.send("Феникс")

    def doBookPoacher(self, _match: []):
        """ Книга браконьера """
        self.send("Браконьер")

    def doBookPunish(self, _match: []):
        """ Книга раправа """
        self.send("Расправа")

    def doBookPrudence(self, _match: []):
        """ Книга расчетливости """
        self.send("Расчетливость")

    def doBookRegen(self, _match: []):
        """ Книга регенерации """
        self.send("Регенерация")

    def doBookReply(self, _match: []):
        """ Книга воздаяния """
        self.send("Воздаяние")

    def doBookScare(self, _match: []):
        """ Книга устрашения """
        self.send("Устрашение")

    def doBookSlash(self, _match: []):
        """ Книга режущего удара """
        self.send("Режущий удар")

    def doBookSmallHeal(self, _match: []):
        """ Книга слабого исцеления """
        self.send("Слабое исцеление")

    def doBookSpeed(self, _match: []):
        """ Книга расторопности """
        self.send("Расторопность")

    def doBookSplit(self, _match: []):
        """ Книга раскола """
        self.send("Раскол")

    def doBookStun(self, _match: []):
        """ Книга ошеломления """
        self.send("Ошеломление")

    def doBookSupersition(self, _match: []):
        """ Книга суеверности """
        self.send("Суеверность")

    def doBookTaran(self, _match: []):
        """ Книга тарана """
        self.send("Таран")

    def doBookMaroder(self, _match: []):
        """ Книга мародера """
        self.send("Мародер")

    def doBookMaps(self, _match: []):
        """ Книга картографа """
        self.send("Картограф")

    def doBookMobility(self, _match: []):
        """ Книга подвижности """
        self.send("Подвижность")
