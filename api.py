import random
from alice_scripts import Skill, request, say, suggest

skill = Skill(__name__)


@skill.script
def run_script():
    end = 17
    yield say(
        'Привет! Ты пришёл почувствовать себя успешным предпринимателем! Рассказать тебе правила игры "Лас-Вегас"?')
    while end > 0:
        answers = request.command
        if answers == 'да':
            yield say(
                'Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. На всех секторах игрового поля отмечены инструкции к дальнейшим действиям. \n Покупка недвижимости: Если вы остановились на поле недвижимости и оно не занято другими участниками, у вас есть право на его покупку или отказ от покупки. \n Владение недвижимостью: Владение зданием дает право взыскивать арендную плату с человека, остановившегося на этом поле.\n «Тюрьма»: Чтобы покинуть этот сектор, необходимо заплатить штраф в 100 $. \n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь банкротом. Вы проигрываете. \n \n \n Готов начать?')
            answers = request.command
            if answers == 'да':
                game = las_vegas()
                end = -1
        else:
            yield say('Не узнав правила, нет смысла даже пытаться. Может всё-таки прочтешь?')


class las_vegas:
    moneyAlica = 200  # Деньги Алисы

    propertyA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # имущество Алисы

    propertyU = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # имущество пользователя

    moneyUser = 200  # Деньги Пользователя

    field_cellA = 0  # Клетка, на которой находится Алиса

    field_cellU = 0  # Клетка, на которой находится пользователь

    max = 40  # количество клеток поля

    bankU = 0  # вклады пользователя (ячейка поля 37)

    bankA = 0  # вклады алисы (ячейка поля 37)

    exchange = 0  # биржа (ячейка поля 13)

    questions = [0, 'Чему равно 2+4-3*2', 'Какое из чисел натуральное? 0, 4, 0.2, 1/2', 'Cтолица Канады',
                 'Столица Южной Кореи',
                 'На какую букву удерание в слове "щавель"',
                 'Какая буква пропущена? Параш..т', 'Кто написал "Горе от ума"?', 'Является ли банан фруктом?',
                 'ЧЕму равна площадь треугольника со сторонами 4 на 3 на 5', 'СКолько в 1км сантиметров?',
                 'Сколько лет длилась Первая Мировая война?']

    answers = [0, 0, 4, 'Оттава', 'Сеул', 'е', 'ю', 'Грибоедов', 'нет', '4.5', '100000', '4']

    fields = [0, 'Cтарт', 'Колесо обозрения "High Roller" Цена: 5$', 'Инвестроры вложили в вас 100$',
              'Ранчо "Casa de Shenandoah" Цена: 5$', 'Шанс ', 'Брат за брата. Отдайте второму игроку 50$',
              'Плотина Гувера Цена: 10$', 'Какая жалость...у вас сломался холодильник -50$',
              'Улица Фримонт-стрит Цена: 10$', 'Аллея Лас-Вегас Цена: 10$', 'Тюрьма. Выход из тюрьмы  - 100$',
              'Парка развлечений "Adventuredome" Цена: 15$',
              'Биржа. Можно оставить на этой клетке 100$,попавший сюда,заберет в 2 раза больше $ или тоже оставит 100$',
              'Музей Shelby American Цена: 15$', 'Национальный музей атомных испытаний Цена: 15$', 'Шанс ',
              'Музей Моб Цена: 20$',
              'Назад в будущее. Игроку будет задан один школьный вопрос. За правильный ответ +50$',
              'Отель-Казино "Белладжио" Цена: 20$', 'Музей Неона Цена: 20$', 'Бесплатный ночлег',
              'Развлекательный комплекс "Луксор Лас-Вегас" Цена: 25$', 'Отправляйтесь на начало',
              'Отель-казино "Париж Лас-Вегас" Цена: 25$', 'Отель-казино "Венецианский Лас-Вегас Цена: 25$"',
              'Мотель. Вы остановились переночевать в мотеле. Заплатите 50$', 'Отель-казино "Wynn" Цена: 30$',
              'Развлекательный комплекс "Сизарс-Пэлас" Цена: 30$',
              'Лотерея. Да вы везунчик, заберите свои законные 95$', 'Отель-казино "Стратосфера Лас-Вегас" Цена: 30$',
              'Отправляйтесь в тюрьму', 'Часовня цветов Цена: 35$', 'Музей мадам Тюссо Цена: 35$',
              'Выберете любую ячейку, на которую отправитесь. Действие этой ячейки на вас не распространиться',
              'Ред-Рок-Каньон Цена: 35$', 'Шанс ',
              'Банк. Вы можете взять деньги под 1,5% или забрать ранее вложенные деньги (с процентами)',
              'Национальный парк "Долина смерти" Цена: 40$', 'Вы такой невнимательный! КАк умудрились потерять 50$?',
              'Сансет Парк Цена: 40$']

    price_field = [0, 200, -5, 100, -5, 0, -50, -10, -50, -10, -10, 0, -15, 0, -15, -15, 0, -20, 0, -20, -20, 0, -25,
                   200,
                   -25, -25, -50, -30, -30, 95, -30, 0, -35, -35, 0, -35, 0, 0, -40, -50, -40]

    chance = [0, 'Вождение в нетрезвом виде. Штраф 20$', 'Вы нашли на улице 15$', 'Вернитесь на 5 ячеек назад',
              'Сегодня у вас день рождения. Подарок  - 25$', 'Вам вернули старый долг 50$',
              'Поход к зубному врачу обошёлся вам в 20$', 'Каждому нужен отдых. ОТправляйтесь на "Бесплатный отдых"',
              'ВЫ купили новый телевизор за 15$', 'Ставка зашла! Выигрыш  - 70$', 'Отправляйтесь на три поля вперед',
              'Нехорошо воровать чужие вещи. Отправляйтесь в тюрьму"',
              'ВЫ купили новый телевизор за 30$']


    price_chance = [0, -20, 15, 0, 25, 50, -20, 0, -15, 70, 0, 0, 30]

    def _init_(self):

        yield say(
            'Первым ходишь ты. Чтобы начать свой ход скажи: "Бросить кубик. ЕСли хочешь построить дом на недвижимостях скажи:"Дом". Ну, начинай же свой первый ход!')
        answers = request.command
        a = 17
        while a > 0:
            if answers != 'бросить кубик':
                yield say('Чтобы начать свой ход скажите: "Бросить кубик"')
                answers = request.command

        if answers == 'бросить кубик':
            random.seed()
            a = -17
            flag = 'true'  # true - ход пользователя, false - алисы

            end = 0

            while end < 0:
                self.cells(self, flag)

                if flag == True & (
                        self.field_cellU == 2 | self.field_cellU == 4 | self.field_cellU == 5 | self.field_cellU == 7 | self.field_cellU == 9 | self.field_cellU == 10 | self.field_cellU == 12 | self.field_cellU == 14 | self.field_cellU == 15 | self.field_cellU == 17 | self.field_cellU == 19 | self.field_cellU == 20 | self.field_cellU == 22 | self.field_cellU == 24 | self.field_cellU == 25 | self.field_cellU == 27 | self.field_cellU == 28 | self.field_cellU == 30 | self.field_cellU == 32 | self.field_cellU == 33 | self.field_cellU == 35 | self.field_cellU == 38 | self.field_cellU == 40):

                    if self.propertyA[self.field_cellU] == 1:
                        yield say(self.fields[self.field_cellA] + '\nВы попали на чужую территорию и заплатили деньги')
                        self.moneyAlica = self.money.Alica + self.price_field[self.field_cellU] / 5
                        self.moneyUser = self.money.User - self.price_field[self.field_cellU] / 5
                        break

                    yield say(self.fields[self.field_cellU] + '\n купить?')
                    choice = request.command
                    if choise == 'да' | choise == 'купить' | choise == 'ага' | choise == 'покупаю':
                        self.moneyUser = self.moneyUser + self.price_field[self.field_cellU]
                        self.propertyU[self.field_cellU] = 1
                        yield say('\n Поздравляем с приобритением!')
                    else:
                        yield say('\n Не всегда стоит покупать')

                if flag == False & (
                        self.field_cellA == 2 | self.field_cellA == 4 | self.field_cellA == 5 | self.field_cellA == 7 | self.field_cellA == 9 | self.field_cellA == 10 | self.field_cellA == 12 | self.field_cellA == 14 | self.field_cellA == 15 | self.field_cellA == 17 | self.field_cellA == 19 | self.field_cellA == 20 | self.field_cellA == 22 | self.field_cellA == 24 | self.field_cellA == 25 | self.field_cellA == 27 | self.field_cellA == 28 | self.field_cellA == 30 | self.field_cellA == 32 | self.field_cellA == 33 | self.field_cellA == 35 | self.field_cellA == 38 | self.field_cellA == 40):

                    if self.propertyU[self.field_cellA] == 1:
                        yield say(
                            self.fields[self.field_cellA] + '\nАлиса попала на вашу территорию и заплатила деньги')
                        self.moneyAlica = self.money.Alica - self.price_field[self.field_cellA] / 5
                        self.moneyUser = self.money.User + self.price_field[self.field_cellA] / 5
                        break

                    choise = random.randint(1, 2)

                    if self.moneyAlica + self.price_field[self.field_cellA] < 0:
                        choise = 2
                        yield say(self.fields[self.field_cellA] + '\n купить? \n Решение Алисы:не покупаю')

                    if choise == 1:
                        yield say(self.fields[self.field_cellA] + '\n купить? \n Решение Алисы:покупаю')
                        self.moneyAlica = self.moneyAlica + self.price_field[self.field_cellA]
                        self.propertyA[self.field_cellA] = 1
                    else:
                        yield say(self.fields[self.field_cellA] + '\n купить? \n Решение Алисы: не покупаю')

                if flag == True & (
                        self.field_cellU == 26 | self.field_cellU == 21 | self.field_cellU == 29 | self.field_cellU == 39 | self.field_cellU == 3 | self.field_cellU == 8):
                    self.moneyUser = self.moneyUser + self.price_field[self.field_cellU]
                    yield say(self.fields[self.field_cellU])

                if flag == False & (
                        self.field_cellA == 26 | self.field_cellA == 21 | self.field_cellA == 29 | self.field_cellA == 39 | self.field_cellA == 3 | self.field_cellA == 8):
                    self.moneyAlica = self.moneyAlica + self.price_field[self.field_cellA]
                    yield say(self.fields[self.field_cellA])

                if flag == True & self.field_cellU == 23:
                    yield say(self.fields[self.field_cellU])
                    self.moneyUser = self.moneyUser + 200
                    self.field_cellU = 1

                if flag == False & self.field_cellA == 23:
                    yield say('\n Алиса ' + self.fields[self.field_cellA])
                    self.moneyAlica = self.moneyAlica + 200
                    self.field_cellA = 1

                if flag == True & self.field_cellU == 31:
                    yield say(self.fields[self.field_cellU])
                    if self.field_cellU > 11:
                        self.moneyUser = self.moneyUser + 200
                    self.field_cellU = 11
                    self.moneyUser = self.moneyUser - 100

                if flag == False & self.field_cellA == 31:
                    yield say('\n Алиса ' + self.fields[self.field_cellA])
                    if self.field_cellA > 11:
                        self.moneyAlica = self.moneyAlica + 200
                    self.field_cellA = 11
                    self.moneyAlica = self.moneyAlica - 100

                if flag == True & self.field_cellU == 6:
                    yield say(self.fields[self.field_cellU])
                    self.moneyUser = self.moneyUser - 50
                    self.moneyAlica = self.moneyAlica + 50

                if flag == False & self.field_cellA == 6:
                    yield say(self.fields[self.field_cellA])
                    self.moneyUser = self.moneyUser + 50
                    self.moneyAlica = self.moneyAlica - 50

                if flag == False & self.field_cellA == 37:
                    if self.moneyAlica < 100:
                        answer = 'взять'
                    if self.moneyAlica > 100 | self.moneyAlica == 100:
                        answer = 'положить'
                    yield say(self.fields[self.field_cellA] + '\n Решение Алисы:' + answer)

                    if answer == 'положить':
                        answer = random.randint(self.moneyAlica / 5, self.moneyAlica / 2)
                        self.moneyAlica = self.moneyAlica - answer
                        self.bank = self.bankA + answer
                    if answer == 'взять':
                        self.moneyAlica = self.moneyAlica + self.bankA

                if flag == True & self.field_cellU == 37:
                    yield say(self.fields[self.field_cellU] + '\n Ваше решение? положить/взять/ничего')
                    answer = request.command
                    if answer == 'положить':
                        yield say('Сколько денег?')
                        answer = request.command
                        self.moneyUser = self.moneyUser - answer
                        self.bankU = self.bankU + answer
                        yield say('\nВы положили женьги в банк под проценты')
                    if answer == 'взять':
                        self.moneyUser = self.moneyUser + self.bankU
                        yield say('\nВы забрали деньги из банка с процентами')
                    else:
                        yield say('\nЯ смотрю, вы, как в старые-добрые времена, храните деньги дома в банке)')

                if flag == True & self.field_cellU == 1:
                    yield say(self.fields[self.field_cellU])

                if flag == False & self.field_cellA == 1:
                    yield say(self.fields[self.field_cellA])

                if flag == True & self.field_cellU == 11:
                    yield say(self.fields[self.field_cellU])
                    self.moneyUser = self.moneyUser - 100

                if flag == False & self.field_cellA == 11:
                    yield say('Алиса попала в ' + self.fields[self.field_cellA])
                    self.moneyAlica = self.moneyAlica - 100

                if self.field_cellU == 18 | self.field_cellA == 18:
                    if flag == 'true':
                        yield say(self.fields[self.field_cellU] + 'Начнём?')
                        answer = request.command
                    self.school(self, flag)

                if flag == False & self.field_cellA == 13:
                    if self.exchange == 0:
                        yield say(self.fields[self.field_cellA] + '\nАлиса оставила деньги на бирже')
                        self.moneyAlica = self.moneyAlica - 100
                        self.exchange = 100
                    if self.exchange != 0:
                        yield say(self.fields[self.field_cellA] + '\nАлиса взяла деньги с биржи')
                        self.moneyAlica = self.moneyAlica + 100
                        self.exchange = 0

                if flag == True & self.field_cellU == 13:
                    if self.exchange == 0:
                        yield say(self.fields[self.field_cellU] + '\nБиржа пуста, вам придется оставить деньги (100$)')
                        self.moneyUser = self.moneyUser - 100
                        self.exchange = 100
                    if self.exchange != 0:
                        yield say(self.fields[self.field_cellU] + '\nВам повезло! Биржа принесла вам 100$')
                        self.moneyUser = self.moneyUser + 100
                        self.exchange = 0

                if self.field_cellU == 5 | self.field_cellA == 5 | self.field_cellU == 16 | self.field_cellA == 16 | self.field_cellU == 36 | self.field_cellA == 36:
                    self.chances(self, flag)

                if flag == False & self.field_cellA == 34:
                    field = random.randint(1, 40)
                    if self.field_cellA > field:
                        self.moneyAlica = self.moneyAlica + 200
                    yield say(self.fields[self.field_cellA] + " Выбор Алисы: " + self.fields[field])
                    self.field_cellA = field

                if flag == True & self.field_cellA == 34:
                    yield say(self.fields[self.field_cellU] + '\n На какую ячейку вы хотите?')
                    field = request.command
                    if self.field_cellU > field:
                        self.moneyUser = self.moneyUser + 200
                    self.field_cellU = field
                    yield say('Вы попали на ' + self.fields[self.field_cellU])

                c = 17

                while c > 0:
                    answer1 = request.command
                    if answer1 != 'Бросить кубик':
                        yield say('Для продолжени игры скажите "бросить кубик" или "мои деньги"')
                    if answer1 == 'Бросить кубик':
                        if self.moneyUser == 0 | self.moneyUser < 0:
                            yield say('Вы обанкротились', end_session=True)
                        if self.moneyAlica == 0 | self.moneyAlica < 0:
                            yield say('Вы победили!', end_session=True)
                        с = -13
                    if answer1 == 'Мои деньги':
                        yield say('Деньги Пользователя: ' + self.moneyUser + '\nДеньги Алисы: ' + self.moneyAlica)

    def chances(self, flag):
        rand = random.randint(1, 12)

        if (
                rand == 1 | rand == 2 | rand == 4 | rand == 5 | rand == 6 | rand == 8 | rand == 9 | rand == 12) & flag == 'true':
            yield say(self.fields[self.field_cellU] + self.chance[rand])
            self.moneyUser = self.moneyUser + self.price_chance[rand]

        if (
                rand == 1 | rand == 2 | rand == 4 | rand == 5 | rand == 6 | rand == 8 | rand == 9 | rand == 12) & flag == 'false':
            yield say('Алиса ' + self.fields[self.field_cellA] + self.chance[rand])
            self.moneyAlica = self.moneyAlica + self.price_chance[rand]

        if rand == 3 & flag == True:
            yield say(self.fields[self.field_cellU] + self.chance[rand])
            self.field_cellU = self.field_cellU - 5

        if rand == 3 & flag == False:
            yield say('Алиса ' + self.fields[self.field_cellA] + self.chance[rand])
            self.field_cellA = self.field_cellA - 5

        if rand == 10 & flag == True:
            yield say(self.fields[self.field_cellU] + self.chance[rand])
            self.field_cellU = self.field_cellU + 3

        if rand == 10 & flag == False:
            yield say('Алиса ' + self.fields[self.field_cellA] + self.chance[rand])
            self.field_cellA = self.field_cellA + 3

        if rand == 11 & flag == True:
            yield say(self.fields[self.field_cellU] + self.chance[rand])
            self.field_cellU = 11
            self.moneyUser = self.moneyUser - 100
        if rand == 11 & flag == False:
            yield say('Алиса ' + self.fields[self.field_cellA] + self.chance[rand])
            self.field_cellA = 11
            self.moneyAlica = self.moneyAlica - 100
        if rand == 7 & flag == True:
            yield say(self.fields[self.field_cellU] + self.chance[rand])
            self.field_cellU = 21
        if rand == 7 & flag == False:
            yield say('Алиса ' + self.fields[self.field_cellA] + self.chance[rand])
            self.field_cellA = 21

    def school(self, flag):
        rand = random.randint(1, 11)
        if flag == False:
            choise = random.randint(1, 2)
            if choise == 1:
                yield say(self.fields[18] + '\n' + self.questions[rand] + '\n Ответ Алисы:' + self.answers[
                    rand] + '\nПравильный ответ')
                self.moneyAlica = self.moneyAlica + 50
            else:
                yield say(self.questions[rand] + '\n Ответ Алисы: я не знаю. НЕ засчитано')

        if flag == True:
            yield say(self.questions[rand])
            answer = request.command
            if answer == self.answers[rand]:
                self.moneyUser = self.moneyUser + 50
                yield say('Правильный ответ')
            else:
                yield say('Неправильный ответ')

    def cells(self, flag):
        field = random.randint(2, 12)
        self.bankU = self.bankU * 1.5
        self.bankA = self.bankA * 1.5

        if flag == False:
            if self.field_cellA + field > self.max:
                self.field_cellA = self.field_cellA + field - self.max
                self.moneyAlica = self.moneyAlica + 200
            else:
                self.field_cellA = self.field_cellA + field
        if flag == True:
            if self.field_cellU + field > self.max:
                self.field_cellU = self.field_cellU + field - self.max
                self.moneyUser = self.moneyUser + 200
            else:
                self.field_cellU = self.field_cellU + field
