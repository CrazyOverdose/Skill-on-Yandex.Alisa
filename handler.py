from __future__ import unicode_literals

import logging
from random import randint
import random

logging.basicConfig(level=logging.DEBUG)


class WinnerError1(Exception):
    pass


class WinnerError2(Exception):
    pass


class las_vegas:
    questions = [0, 'Чему равно 2+4-3*2', 'Какое из чисел натуральное? 0, 4, 0.2, 1/2', 'Cтолица Канады',
                 'Столица Южной Кореи',
                 'На какую букву ударание в слове "щавель"',
                 'Какая буква пропущена? Параш..т', 'Кто написал "Горе от ума"?', 'Является ли банан фруктом?',
                 'Чему равна площадь треугольника со сторонами 4 на 3 на 5', 'СКолько в 1км сантиметров?',
                 'Сколько лет длилась Первая Мировая война?']

    answers = [0, 0, 4, 'Оттава', 'Сеул', 'е', 'ю', 'Грибоедов', 'нет', '4.5', '100000', '4']

    fields = [0, 'Cтарт', 'Колесо обозрения "High Roller" Цена: 5$', 'Инвестроры вложили в вас 100$',
              'Ранчо "Casa de Shenandoah" Цена: 5$', 'Шанс ', 'Брат за брата. Отдайте второму игроку 50$',
              'Плотина Гувера Цена: 10$', 'Какая жалость...у вас сломался холодильник -50$',
              'Улица Фримонт-стрит Цена: 10$', 'Аллея Лас-Вегас Цена: 10$', 'Тюрьма. Выход из тюрьмы  - 100$',
              'Парка развлечений "Adventuredome" Цена: 15$',
              'Биржа. Если она пуста, то должен оставить 100$, если нет,то вправе забрать в 2 раза больше, чем на ней '
              'есть или оставить еще 100',
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
              'Банк. Вы можете положить деньги (каждый круг +150$) (скажите, сколько денег хотите положить), забрать ранее вложенные деньги (с процентами) Для этого скажите "забрать"',
              'Национальный парк "Долина смерти" Цена: 40$', 'Вы такой невнимательный! КАк умудрились потерять 50$?',
              'Сансет Парк Цена: 40$']

    price_field = [0, 200, -5, 100, -5, 0, -50, -10, -50, -10, -10, -200, -15, 0, -15, -15, 0, -20, 0, -20, -20, 0, -25,
                   200,
                   -25, -25, -50, -30, -30, 95, -30, 0, -35, -35, 0, -35, 0, 0, -40, -50, -40]

    price_foreign_field = [0, 2, -2, 100, -2, -2, -50, -4, -50, -4, -4, 0, -6, 0, -6, -6, 0, -10, 0, -10, -10, 0, -14,
                           200,
                           -14, -14, -50, -16, -16, 95, -16, 0, -18, -18, 0, -18, 0, 0, -25, -50, -25]

    chance = [0, 'Вождение в нетрезвом виде. Штраф 20$', 'Вы нашли на улице 15$', 'Вернитесь на 5 ячеек назад',
              'Сегодня у вас день рождения. Подарок  - 25$', 'Вам вернули старый долг 50$',
              'Поход к зубному врачу обошёлся вам в 20$', 'Каждому нужен отдых. ОТправляйтесь на "Бесплатный отдых"',
              'ВЫ купили новый телевизор за 15$', 'Ставка зашла! Выигрыш  - 70$', 'Отправляйтесь на три поля вперед',
              'Нехорошо воровать чужие вещи. Отправляйтесь в тюрьму"',
              'ВЫ купили новый телевизор за 30$']

    price_chance = [0, -20, 15, 0, 25, 50, -20, 0, -15, 70, 0, 0, 30]


FIELD = ['поле', 'карта', 'ячейки']

MONEY = ['деньги', 'моиденьги', 'сколькоуменяденег', 'сколькоденег', 'финансы', 'сбережения']

WORDS = ['броситькубик', 'я хожу', 'го', 'давайиграть', 'играть', 'начать']

ENDING_WORDS = ['новаяигра', 'выход', 'начатьновуюигру']

BURSEtake = ['взять', 'забрать', 'взятьденьги', 'забратьденьги', ]

BURSEgive = ['оставить', 'отдать', 'отдатьденьги', 'положить', 'оставитьденьги', 'положитьденьги', ]

PLACE = ['мояячейка', 'гдея', 'моеположение', 'накакойяячейке', 'клетка', 'мояклетка', 'накакойяклетке']

RULES = ['правила', 'какиграть', 'описание', 'описаниеигры']

MAP = ['ячейки', 'карта', 'поле', 'описаниеячеек']

ALL_WORDS = WORDS + ENDING_WORDS + MONEY + FIELD + PLACE + RULES + MAP


# Функция для непосредственной обработки диалога.
def handle_dialog(request, response, user_storage):
    # response.user_id
    game = las_vegas()
    random.seed()
    if request.is_new_session:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        user_storage = {
            "propertyA": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # имущество Алисы
            "propertyU": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            # имущество пользователя
            "moneyU": 200,  # Деньги Пользователя
            "moneyA": 200,  # Деньги Алисы
            "field_cellA": 18,  # Клетка, на которой находится Алиса
            "field_cellU": 18,  # Клетка, на которой находится пользователь
            "bankU": 0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0,  # вклады алисы (ячейка поля 37)
            "exchange": float(0),  # биржа (ячейка поля 13)
            "user_id": request.user_id,
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": False

        }

        global backup_turn

        backup_turn = user_storage

        # Приветствие
        response.set_text(
            'Добро пожаловать в "Лас-Вегас"! Ты пришёл почувствовать себя успешным предпринимателем!'
            'Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по '
            'полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. '
            '\n Покупка недвижимости: Если '
            'вы остановились на поле недвижимости и оно не занято другими участниками, у вас есть право на '
            'его покупку или отказ от покупки. \n Владение недвижимостью: Владение зданием дает право '
            'взыскивать арендную плату с человека, остановившегося на этом поле.\n «Тюрьма»: Чтобы покинуть '
            'этот сектор, необходимо заплатить штраф в 100 $. \n Если вам не хватает средств на какие-то '
            'обязательные выплаты, вы становитесь банкротом. \n \n Чтобы начать новую игру наберите "новая игра", '
            'чтобы сделать свой ход наберите "бросить кубик"')
        # Выходим из функции и ждем ответа
        return response, user_storage

    # Обрабатываем ответ пользователя.
    user_message = request.command.lower().strip().replace(' ', '')

    try:
        if float(user_storage["moneyU"]) < 0:
            raise WinnerError1

        if float(user_storage["moneyA"]) < 0:
            raise WinnerError2

        if int(user_storage["school"]) != 0:
            if str(user_message) == str(game.answers[int(user_storage["school"])]):
                response.set_text('Правильный ответ')
                user_storage["moneyU"] = float(user_storage["moneyU"]) + 50
            else:
                response.set_text('Неправильный ответ')
            user_storage["school"] = 0
            return response, user_storage

        if bool(user_storage["choice"]):
            if user_message in BURSEtake:
                user_storage["moneyU"] = float(user_storage["moneyU"]) + float(user_storage["exchange"]) * 1.5
                response.set_text('Вы взяли ' + str(user_storage["exchange"]) + ' $ с биржи')
                user_storage["exchange"] = 0

            if user_message in BURSEgive:
                user_storage["moneyU"] = float(user_storage["moneyU"]) - 100
                user_storage["exchange"] = float(user_storage["exchange"]) + 100
                response.set_text('Вы оставили 100$ на бирже')

            if user_message not in BURSEgive + BURSEtake:
                response.set_text('Иногда ничего не делать - лучшее решение')
            user_storage["choice"] = False
            return response, user_storage

        if int(user_storage["property"]) != 0:
            if str(user_message) == 'купить':
                user_storage["moneyU"] = float(user_storage["moneyU"]) + float(
                    game.price_field[int(user_storage["field_cellU"])])
                user_storage["propertyU"][int(user_storage["property"])] = 1
                response.set_text('Поздравляю с приобретением! ')
            else:
                response.set_text('Может, это действительно не лучшее вложение денег')
            user_storage["property"] = 0
            return response, user_storage

        if user_message in ALL_WORDS:
            cube = 0

            if user_message in PLACE:
                response.set_text('Вы находитесь на ' + str(user_storage["field_cellU"]) + ' ячейке \n Алиса на ' + str(
                    user_storage["field_cellA"]))

                # Проверка наличия слова в словах о начале игры
            if user_message in ENDING_WORDS:
                text = ''
                user_storage = end(request, response, text)

            if user_message in RULES:
                response.set_text('Каждый участник бросает кубик и в зависимости от выпавшего количества '
                                  'очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – '
                                  'не обанкротиться. \n Если вы остановились на поле недвижимости и оно не '
                                  'занято другими участниками, у вас есть право на его покупку или отказ от покупки. \n Владение зданием '
                                  'дает право взыскивать арендную плату с человека, '
                                  'остановившегося на этом поле.\n «Тюрьма»: Чтобы покинуть этот сектор, необходимо заплатить '
                                  'штраф в 100 $. \n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь '
                                  'банкротом. \n \n Чтобы начать новую игру наберите "новая игра", чтобы сделать свой ход '
                                  'наберите "бросить кубик"')

            if user_message in MAP:
                response.set_text(
                    '1 - Cтарт\n2 - Колесо обозрения "High Roller"\n3 - Лучший предприниматель\n'
                    '4 - Ранчо "Casa de Shenandoah"\n5; 16; 36 - Шанс\n6 - Брат за брата\n'
                    '7 - Плотина Гувера\n 8 - Сломанный холодильник\n'
                    '9 - Улица Фримонт-стрит\n 10 - Аллея Лас-Вегас\n 11 - Тюрьма'
                    '\n 12 - Парка развлечений "Adventuredome"\n'
                    '13 - Биржа\n'
                    '14 - Музей Shelby American\n 15 - Национальный музей атомных испытаний\n'
                    '17 - Музей Моб\n '
                    '18 - Назад в будущее\n'
                    '19 - Отель-Казино "Белладжио"\n20 - Музей Неона\n  21 - Бесплатный ночлег\n'
                    '22 - Развлекательный комплекс "Луксор Лас-Вегас"\n 23 - Отправляйтесь на начало\n'
                    '24 - Отель-казино "Париж Лас-Вегас"\n25 - Отель-казино "Венецианский Лас-Вегас\n'
                    '26 - Мотель\n 27 - Отель-казино "Wynn"\n'
                    '28 - Развлекательный комплекс "Сизарс-Пэлас"\n'
                    '29 - Лотерея\n 30 - Отель-казино "Стратосфера Лас-Вегас"\n'
                    '31 - Отправляйтесь в тюрьму\n 32 - Часовня цветов\n 33 - Музей мадам Тюссо\n'
                    '34 - Выберете любую ячейку, на которую отправитесь.\n'
                    '35 - Ред-Рок-Каньон\n'
                    '37 - Банк\n'
                    '38 - Национальный парк "Долина смерти"\n 39 - Потеря\n'
                    '40 - Сансет Парк')

            if user_message in MONEY:
                response.set_text(
                    'Ваши деньги ' + str(user_storage["moneyU"]) + '  Деньги Алисы ' + str(user_storage["moneyA"]))

            if user_message in WORDS:
                if not bool(user_storage["users_turn"]):
                    if int(cube) + int(user_storage["field_cellA"]) > 40:
                        user_storage["moneyA"] = float(user_storage["moneyA"]) + 200
                        user_storage["bankA"] = float(user_storage["bankA"]) * 1.2
                        user_storage["field_cellA"] = int(user_storage["field_cellA"]) + int(cube) - 40

                    if int(cube) + int(user_storage["field_cellA"]) < 40:
                        user_storage["field_cellA"] = int(user_storage["field_cellA"]) + int(cube)

                    if int(user_storage["field_cellA"]) == 23:
                        response.set_text('Ход Алисы \n' + str(game.fields[int(user_storage["field_cellA"])]))
                        user_storage["moneyA"] = float(user_storage["moneyA"]) + 200
                        user_storage["field_cellA"] = 1

                    if int(user_storage["field_cellA"]) == 26 or int(user_storage["field_cellA"]) == 21 or int(
                            user_storage["field_cellA"]) == 29 or int(user_storage["field_cellA"]) == 39 or int(
                        user_storage["field_cellA"]) == 3 or int(user_storage["field_cellA"]) == 8 or int(
                        user_storage["field_cellA"]) == 11:
                        user_storage["moneyA"] = float(user_storage["moneyA"]) + float(
                            game.price_field[int(user_storage["field_cellA"])])
                        response.set_text('Ход Алисы \n' + str(game.fields[int(user_storage["field_cellA"])]))

                    if int(user_storage["field_cellA"]) == 31:
                        response.set_text('Ход Алисы \n' + str(game.fields[int(user_storage["field_cellA"])]))
                        user_storage["moneyA"] = float(user_storage["moneyA"]) + 100
                        user_storage["field_cellA"] = 11

                    if int(user_storage["field_cellA"]) == 6:
                        response.set_text(str('Ход Алисы \n' + game.fields[int(user_storage["field_cellA"])]))
                        user_storage["moneyA"] = float(user_storage["moneyA"]) - 50
                        user_storage["moneyU"] = float(user_storage["moneyU"]) + 50

                    if int(user_storage["field_cellA"]) == 1:
                        response.set_text('Ход Алисы \n' + str(game.fields[int(user_storage["field_cellA"])]))

                    if int(user_storage["field_cellA"]) == 2 or int(user_storage["field_cellA"]) == 4 or int(
                            user_storage["field_cellA"]) == 5 or int(user_storage["field_cellA"]) == 7 or int(
                        user_storage["field_cellA"]) == 9 or int(user_storage["field_cellA"]) == 10 or int(
                        user_storage["field_cellA"]) == 12 or int(user_storage["field_cellA"]) == 14 or int(
                        user_storage["field_cellA"]) == 15 or int(user_storage["field_cellA"]) == 17 or int(
                        user_storage["field_cellA"]) == 19 or int(user_storage["field_cellA"]) == 20 or int(
                        user_storage["field_cellA"]) == 22 or int(user_storage["field_cellA"]) == 24 or int(
                        user_storage["field_cellA"]) == 25 or int(user_storage["field_cellA"]) == 27 or int(
                        user_storage["field_cellA"]) == 28 or int(user_storage["field_cellA"]) == 30 or int(
                        user_storage["field_cellA"]) == 32 or int(user_storage["field_cellA"]) == 33 or int(
                        user_storage["field_cellA"]) == 35 or int(user_storage["field_cellA"]) == 38 or int(
                        user_storage["field_cellA"]) == 40:

                        a = int(conversion(int(user_storage["field_cellA"])))

                        b = int(randint(1, 2))

                        if int(user_storage["moneyA"]) < 45:
                            b = 2

                        if int(user_storage["propertyU"][a]) == 1:
                            response.set_text('Ход Алисы \n' +
                                              'Алиса попала на ваш участок: ' + str(
                                game.fields[int(user_storage["field_cellA"])]))
                            user_storage["moneyA"] = float(user_storage["moneyA"]) + float(
                                game.price_foreign_field[int(user_storage["field_cellA"])])
                            user_storage["moneyU"] = float(user_storage["moneyU"]) - float(
                                game.price_foreign_field[int(user_storage["field_cellA"])])

                        if int(user_storage["propertyA"][a]) == 1:
                            response.set_text('Ход Алисы \n' +
                                              'Алиса попала на свою территорию: ' + str(
                                game.fields[int(user_storage["field_cellA"])]))

                        if int(user_storage["propertyA"][a]) == 0 and int(user_storage["propertyU"][a]) == 0:
                            if b == 1:
                                response.set_text('Ход Алисы \n' + str(
                                    game.fields[int(user_storage["field_cellA"])]) + ' и решила купить')
                                user_storage["moneyA"] = float(user_storage["moneyA"]) + float(
                                    game.price_field[int(user_storage["field_cellA"])])
                                user_storage["propertyA"][a] = 1
                            else:
                                response.set_text('Ход Алисы \n' +
                                                  'Алиса попала: ' + str(
                                    game.fields[int(user_storage["field_cellA"])]) + ' и решила не покупать')

                    if int(user_storage["field_cellA"]) == 13:
                        y = randint(1, 2)
                        if float(user_storage["exchange"]) == 0:
                            response.set_text('Ход Алисы \n' +
                                              str(game.fields[int(
                                                  user_storage["field_cellA"])]) + '\nАлиса оставила деньги на бирже')
                            user_storage["moneyA"] = float(user_storage["moneyA"]) - 100
                            user_storage["exchange"] = 100

                        if float(user_storage["exchange"]) != 0:

                            if float(user_storage["moneyA"]) < 150:
                                y = 2

                            if int(y) == 2:
                                response.set_text('Ход Алисы \n' +
                                                  str(game.fields[int(
                                                      user_storage["field_cellA"])]) + '\nАлиса взяла деньги с биржи')
                                user_storage["moneyA"] = float(user_storage["moneyA"]) + 1.5 * float(
                                    user_storage["exchange"])
                                user_storage["exchange"] = 0

                            if int(y) == 1:
                                response.set_text('Ход Алисы \n' +
                                                  str(game.fields[int(
                                                      user_storage[
                                                          "field_cellA"])]) + '\nАлиса оставила деньги на бирже')
                                user_storage["moneyA"] = float(user_storage["moneyA"]) - 100
                                user_storage["exchange"] = user_storage["exchange"] + 100

                    if int(user_storage["field_cellA"]) == 18:
                        response.set_text('' + str(school(user_storage, game)))

                    user_storage["users_turn"] = True
                    return response, user_storage

                if bool(user_storage["users_turn"]):
                    if int(cube) + int(user_storage["field_cellU"]) > 40:
                        user_storage["moneyU"] = float(user_storage["moneyU"]) + 200
                        user_storage["bankU"] = float(user_storage["bankU"]) * 1.2
                        user_storage["field_cellU"] = int(user_storage["field_cellU"]) + int(cube) - 40

                    if int(cube) + int(user_storage["field_cellU"]) < 40:
                        user_storage["field_cellU"] = int(user_storage["field_cellU"]) + int(cube)

                    if int(user_storage["field_cellU"]) == 23:
                        response.set_text('Ваш ход \n' + str(game.fields[int(user_storage["field_cellU"])]))
                        user_storage["moneyU"] = float(user_storage["moneyU"]) + 200
                        user_storage["field_cellU"] = 1

                    if int(user_storage["field_cellU"]) == 26 or int(user_storage["field_cellU"]) == 21 or int(
                            user_storage["field_cellU"]) == 29 or int(user_storage["field_cellU"]) == 39 or int(
                        user_storage["field_cellU"]) == 3 or int(user_storage["field_cellU"]) == 8 or int(
                        user_storage["field_cellU"]) == 11:
                        user_storage["moneyU"] = float(user_storage["moneyU"]) + float(
                            game.price_field[int(user_storage["field_cellU"])])
                        response.set_text('Ваш ход \n' + str(game.fields[int(user_storage["field_cellU"])]))

                    if int(user_storage["field_cellU"]) == 31:
                        response.set_text('Ваш ход \n' + str(game.fields[int(user_storage["field_cellU"])]))
                        user_storage["moneyU"] = float(user_storage["moneyU"]) + 100
                        user_storage["field_cellU"] = 11

                    if int(user_storage["field_cellU"]) == 6:
                        response.set_text('Ваш ход \n' + str(game.fields[int(user_storage["field_cellU"])]))
                        user_storage["moneyU"] = float(user_storage["moneyU"]) - 50
                        user_storage["moneyA"] = float(user_storage["moneyA"]) + 50

                    if int(user_storage["field_cellU"]) == 1:
                        response.set_text('Ваш ход \n' + str(game.fields[int(user_storage["field_cellU"])]))

                    if int(user_storage["field_cellU"]) == 2 or int(user_storage["field_cellU"]) == 4 or int(
                            user_storage["field_cellU"]) == 5 or int(user_storage["field_cellU"]) == 7 or int(
                        user_storage["field_cellU"]) == 9 or int(user_storage["field_cellU"]) == 10 or int(
                        user_storage["field_cellU"]) == 12 or int(user_storage["field_cellU"]) == 14 or int(
                        user_storage["field_cellU"]) == 15 or int(user_storage["field_cellU"]) == 17 or int(
                        user_storage["field_cellU"]) == 19 or int(user_storage["field_cellU"]) == 20 or int(
                        user_storage["field_cellU"]) == 22 or int(user_storage["field_cellU"]) == 24 or int(
                        user_storage["field_cellU"]) == 25 or int(user_storage["field_cellU"]) == 27 or int(
                        user_storage["field_cellU"]) == 28 or int(user_storage["field_cellU"]) == 30 or int(
                        user_storage["field_cellU"]) == 32 or int(user_storage["field_cellU"]) == 33 or int(
                        user_storage["field_cellU"]) == 35 or int(user_storage["field_cellU"]) == 38 or int(
                        user_storage["field_cellU"]) == 40:

                        a = int(conversion(int(user_storage["field_cellU"])))
                        if int(user_storage["propertyA"][int(a)]) == 1:
                            response.set_text(
                                str('Ваш ход \n' + game.fields[
                                    int(user_storage[
                                            "field_cellU"])]) + ' \nВы попали на недвижимость Алисы')
                            user_storage["moneyU"] = float(user_storage["moneyU"]) + game.price_foreign_field[
                                int(user_storage["field_cellU"])]
                            user_storage["moneyA"] = float(user_storage["moneyA"]) - game.price_foreign_field[
                                int(user_storage["field_cellU"])]

                        if int(user_storage["propertyU"][int(a)]) == 1:
                            response.set_text(
                                str('Ваш ход \n' + game.fields[
                                    int(user_storage[
                                            "field_cellU"])]) + ' \nВы попали на свою территорию')

                        if int(user_storage["propertyU"][int(a)]) == 0 and int(user_storage["propertyA"][int(a)]) == 0:
                            response.set_text(
                                str('Ваш ход \n' + game.fields[int(
                                    user_storage["field_cellU"])]) + ' Если хотите приобрести, введите (купить)')
                            user_storage["property"] = int(a)

                    if int(user_storage["field_cellU"]) == 13:
                        if float(user_storage["exchange"]) != 0:
                            response.set_text('Ваш ход \n' + str(game.fields[int(user_storage["field_cellU"])]))
                            user_storage["choice"] = True

                        if float(user_storage["exchange"]) == 0:
                            response.set_text('Ваш ход \n' +
                                              str(game.fields[int(
                                                  user_storage["field_cellU"])]) + '\n Биржа пуста, вы оставили деньги')
                            user_storage["moneyU"] = float(user_storage["moneyU"]) - 100
                            user_storage["exchange"] = 100

                    if int(user_storage["field_cellU"]) == 18:
                        user_storage = school(request, response,user_storage)

                    user_storage["users_turn"] = False
                    return response, user_storage

        else:
            response.set_text("Простите, но я вас не поняла.")

    except WinnerError1:
        text = 'Мне очень жаль, но вы проиграли \n'
        user_storage = end(request, response, text)

    except WinnerError2:
        text = 'Поздравляю, вы победили! \n '
        user_storage = end(request, response, text)

    # В любом случае
    return response, user_storage


# Шансы
def chances(user_storage, game):
    rand = int(randint(1, 12))
    answer = ''
    if int(rand) == 1 or int(rand) == 2 or int(rand) == 4 or int(rand) == 5 or int(rand) == 6 or int(rand) == 8 or int(
            rand) == 9 or int(rand) == 12:
        if bool(user_storage["users_turns"]):
            user_storage["moneyU"] = float(user_storage["moneyU"]) + float(game.price_chance[int(rand)])
        if not bool(user_storage["users_turns"]):
            user_storage["moneyA"] = float(user_storage["moneyA"]) + float(game.price_chance[int(rand)])

    if int(rand) == 3:
        if bool(user_storage["users_turns"]):
            user_storage["field_cellU"] = int(user_storage["field_cellU"]) - 5

        if not bool(user_storage["users_turns"]):
            user_storage["field_cellA"] = int(user_storage["field_cellA"]) - 5

    if int(rand) == 10:
        if bool(user_storage["users_turns"]):
            user_storage["field_cellU"] = int(user_storage["field_cellU"]) + 3

        if not bool(user_storage["users_turns"]):
            user_storage["field_cellA"] = int(user_storage["field_cellA"]) + 3

    if int(rand) == 11:
        if bool(user_storage["users_turns"]):
            user_storage["field_cellU"] = 11
            user_storage["moneyU"] = float(user_storage["moneyU"]) - 100

        if not bool(user_storage["users_turns"]):
            user_storage["field_cellA"] = 11
            user_storage["moneyA"] = float(user_storage["moneyA"]) - 100

    if int(rand) == 7:
        if bool(user_storage["users_turns"]):
            user_storage["field_cellU"] = 21

        if not bool(user_storage["users_turns"]):
            user_storage["field_cellA"] = 21

    if not bool(user_storage["users_turns"]):
        answer = str('Ход Алисы \n ' + str(game.fields[int(user_storage["field_cellA"])]) + str(game.chance[int(rand)]))

    if bool(user_storage["users_turns"]):
        answer = str('Ваш ход \n ' + str(game.fields[int(user_storage["field_cellU"])]) + str(game.chance[int(rand)]))

    answer = 'тута'
    return answer


# Начало новой игры
def end(request, response, text):
    game = las_vegas()
    random.seed()

    response.set_text(str(text) +
                      'Давай напомню правила: Каждый участник бросает кубик и в зависимости от выпавшего количества '
                      'очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – '
                      'не обанкротиться. \n Если вы остановились на поле недвижимости и оно не '
                      'занято другими участниками, у вас есть право на его покупку или отказ от покупки. \n Владение зданием '
                      'дает право взыскивать арендную плату с человека, '
                      'остановившегося на этом поле.\n «Тюрьма»: Чтобы покинуть этот сектор, необходимо заплатить '
                      'штраф в 100 $. \n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь '
                      'банкротом. \n \n Чтобы начать новую игру наберите "новая игра", чтобы сделать свой ход '
                      'наберите "бросить кубик"')

    user_storage = {
        "propertyA": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # имущество Алисы
        "propertyU": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # имущество пользователя
        "moneyU": 200,  # Деньги Пользователя
        "moneyA": 200,  # Деньги Алисы
        "field_cellA": 40,  # Клетка, на которой находится Алиса
        "field_cellU": 40,  # Клетка, на которой находится пользователь
        "bankU": 0,  # вклады пользователя (ячейка поля 37)
        "bankA": 0,  # вклады алисы (ячейка поля 37)
        "exchange": 0,  # биржа (ячейка поля 13)
        "user_id": request.user_id,
        "users_turn": False,
        "bank": False,
        "property": 0,
        "go": False,
        "school": 0
    }

    return user_storage


def school(request, response, user_storage):
    game = las_vegas()
    rand = int(randint(1, 11))
    if not bool(user_storage["users_turns"]):
        choise = int(randint(1, 2))
        if choise == 1:
            user_storage["moneyA"] = float(user_storage["moneyA"]) + 50
            response.set_text(
                'Ход Алисы \n ' + str(game.fields[18]) + '\n' + str(
                    game.questions[int(rand)]) + '\n Ответ Алисы:' + str(
                    game.answers[int(rand)]) + '\nПравильный ответ')
        else:
            response.set_text(
                str('Ход Алисы \n ' + game.fields[18]) + '\n' + str(
                    game.questions[int(rand)]) + '\n Ответ Алисы: я не знаю. НЕ засчитано')

    if bool(user_storage["users_turns"]):
        user_storage["flag"] = int(rand)
        response.set_text( str(game.fields[18]) + '\n' + str(game.questions[int(rand)]))

    return user_storage


def conversion(a):
    if a == 2:
        a = 1
    if a == 4:
        a = 2
    if a == 7:
        a = 3
    if a == 9:
        a = 4
    if a == 10:
        a = 5
    if a == 12:
        a = 6
    if a == 14:
        a = 7
    if a == 15:
        a = 8
    if a == 17:
        a = 9
    if a == 19:
        a = 10
    if a == 20:
        a = 11
    if a == 22:
        a = 12
    if a == 24:
        a = 13
    if a == 25:
        a = 14
    if a == 27:
        a = 15
    if a == 28:
        a = 16
    if a == 30:
        a = 17
    if a == 32:
        a = 18
    if a == 33:
        a = 19
    if a == 38:
        a = 20
    if a == 40:
        a = 21
    return int(a)
