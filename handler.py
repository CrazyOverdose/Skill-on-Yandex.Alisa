from __future__ import unicode_literals

import logging
from random import randint

logging.basicConfig(level=logging.DEBUG)


class WinnerError(Exception):
    pass


class las_vegas:
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
              'Биржа. Нужно оставить на этой клетке 200$,попавший сюда,заберет в 2 раза больше $',
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
              'Банк. Вы можете взять деньги под 1,5% (скажите, сколько денег хотите положить), забрать ранее вложенные деньги (с процентами) Для этого скажите "забрать"',
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


MONEY = ['деньги', 'моиденьги', 'сколькоуменяденег', 'сколькоденег', 'финансы', 'сбережения']

WORDS = ['броситькубик', 'я хожу', 'го', 'давайиграть', 'играть', 'начать']

ENDING_WORDS = ['новаяигра', 'выход', 'начатьновуюигру']

ALL_WORDS = WORDS + ENDING_WORDS + MONEY


# Функция для непосредственной обработки диалога.
def handle_dialog(request, response, user_storage):
    # response.user_id
    game = las_vegas()
    if request.is_new_session:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        user_storage = {
            "propertyA": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0],  # имущество Алисы
            "propertyU": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0],  # имущество пользователя
            "moneyU": 200,  # Деньги Пользователя
            "moneyA": 200,  # Деньги Алисы
            "field_cellA": 0,  # Клетка, на которой находится Алиса
            "field_cellU": 0,  # Клетка, на которой находится пользователь
            "bankU": 0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0,  # вклады алисы (ячейка поля 37)
            "exchange": 0,  # биржа (ячейка поля 13)
            "user_id": request.user_id,
            "users_turn": True,
            "bank": False,
            "property": 0,
            "go": False,
            "school": 0
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

    alena = 17

    text = ' '

    if alena == 17:

        if user_storage["school"] != 0:
            if user_message == game.answers[user_storage["school"]]:
                response.set_text('Правильный ответ')
                user_storage["moneyU"] = user_storage["moneyU"] + 50
            else:
                response.set_text('Неправильный ответ')
            user_storage["school"] = 0
            return response, user_storage

        if user_storage["property"] != 0:
            if user_message == "купить":
                user_storage["moneyU"] = user_storage["moneyU"] + game.fields[user_storage["field_cellU"]]
                user_storage["propertyU"][user_storage["property"]] = 1
                response.set_text('Поздравляем с приобретерием!')
            else:
                response.set_text('Может, это действиельно не лучшее вложение денег')
            user_storage["property"] = 0
            return response, user_storage

        if user_storage["bank"]:
            if user_message == "забрать":
                response.set_text('Вы забрали деньги')
                user_storage["moneyU"] = user_storage["moneyU"] + user_storage["bankU"]
                user_storage["bankU"] = 0

            if user_message.is_integer():
                response.set_text('Вы положили деньги под проценты')
                user_storage["moneyU"] = user_storage["moneyU"] - user_message.is_integer()
                user_storage["bankU"] = user_storage["bankU"] + user_message.is_integer()
            else:
                response.set_text('Ну, не всем становиться миллионерами')
            user_storage["bank"] = False
            return response, user_storage

        if user_storage["go"]:
            if user_message.is_integer():
                response.set_text('Вы переместились на ячейку: ' + game.fields[user_message.is_integer()])
                user_storage["field_cellU"] = user_message.is_integer()
                if user_storage["field_cellU"] > user_message.is_integer():
                    user_storage["moneyU"] = user_storage["moneyU"] + 200
            else:
                response.set_text('ВЫ решили остаться на этой ячейке')
            user_storage["go"] = False
            return response, user_storage

        # Проверка слова в допустимых словах
        if user_message in ALL_WORDS:
            cube = randint(2, 12)

            if user_storage["moneyU"] <= 0:
                text = 'Мне очень жаль, но вы проиграли'
                user_storage = end(request, response)

            if user_storage["moneyA"] <= 0:
                text = 'Мне очень жаль, но вы проиграли'
                user_storage = end(request, response)

            # Проверка наличия слова в словах о начале игры
            if user_message in ENDING_WORDS:
                user_storage = end(request, response)

            if user_message in MONEY:
                text1 = str(user_storage["moneyU"])
                text2 = str(user_storage["moneyU"])
                text3 = 'Ваши деньги ' + text1 + 'Деньги Алисы ' + text2
                response.set_text(text3)

            # Если Пользователь
            if user_message in WORDS:
                if user_storage["users_turn"]:
                    if cube + user_storage["field_cellU"] > 40:
                        user_storage["moneyU"] = user_storage["moneyU"] + 200
                        user_storage["bankU"] = user_storage["bankU"] * 1.5
                        user_storage["field_cellU"] = user_storage["field_cellU"] + cube - 40

                    if cube + user_storage["field_cellA"] < 40:
                        user_storage["field_cellU"] = user_storage["field_cellU"] + cube

                    if user_storage["field_cellU"] == 2 | user_storage["field_cellU"] == 4 | user_storage[
                        "field_cellU"] == 5 | user_storage["field_cellU"] == 7 | user_storage["field_cellU"] == 9 | \
                            user_storage["field_cellU"] == 10 | user_storage["field_cellU"] == 12 | user_storage[
                        "field_cellU"] == 14 | user_storage["field_cellU"] == 15 | user_storage["field_cellU"] == 17 | \
                            user_storage["field_cellU"] == 19 | user_storage["field_cellU"] == 20 | user_storage[
                        "field_cellU"] == 22 | user_storage["field_cellU"] == 24 | user_storage["field_cellU"] == 25 | \
                            user_storage["field_cellU"] == 27 | user_storage["field_cellU"] == 28 | user_storage[
                        "field_cellU"] == 30 | user_storage["field_cellU"] == 32 | user_storage["field_cellU"] == 33 | \
                            user_storage["field_cellU"] == 35 | user_storage["field_cellU"] == 38 | user_storage[
                        "field_cellU"] == 40:
                        a = conversion(user_storage["field_cellA"])
                        response.set_text(
                            game.fields[user_storage["field_cellA"]] + 'Если хотите приобрести, введите (купить)')

                        user_storage["property"] = a

                    if user_storage["field_cellU"] == 26 | user_storage["field_cellU"] == 21 | user_storage[
                        "field_cellU"] == 29 | user_storage["field_cellU"] == 39 | user_storage["field_cellU"] == 3 | \
                            user_storage[
                                "field_cellU"] == 8:
                        user_storage["moneyU"] = user_storage["moneyU"] + game.price_field[user_storage["field_cellU"]]
                        response.set_text(game.fields[user_storage["field_cellU"]])

                    if user_storage["field_cellU"] == 23:
                        response.set_text(game.fields[user_storage["field_cellU"]])
                        user_storage["moneyU"] = user_storage["moneyU"] + 200
                        user_storage["field_cellU"] = 1

                    if user_storage["field_cellU"] == 31:
                        response.set_text(game.fields[user_storage["field_cellU"]])
                        user_storage["moneyU"] = user_storage["moneyU"] + 100
                        user_storage["field_cellU"] = 11

                    if user_storage["field_cellU"] == 6:
                        response.set_text(game.fields[user_storage["field_cellU"]])
                        user_storage["moneyU"] = user_storage["moneyU"] - 50
                        user_storage["moneyA"] = user_storage["moneyA"] + 50

                    if user_storage["field_cellU"] == 37:
                        response.set_text(game.fields[user_storage["field_cellU"]])
                        user_storage["bank"] = True

                    if user_storage["field_cellU"] == 1:
                        response.set_text(game.fields[user_storage["field_cellU"]])

                    if user_storage["field_cellU"] == 11:
                        response.set_text('\n Алиса попала в ' + game.fields[user_storage["field_cellU"]])
                        user_storage["moneyU"] = user_storage["moneyU"] - 100

                    if user_storage["field_cellU"] == 18:
                        response.set_text(game.fields[user_storage["field_cellU"]])
                        response.set_text(school(user_storage, game))

                    if user_storage["field_cellU"] == 13:
                        if user_storage["exchange"] == 0:
                            response.set_text(
                                game.fields[
                                    user_storage["field_cellU"]] + ' Биржа пуста, значит вы должны оставить 200$')
                            user_storage["moneyU"] = user_storage["moneyU"] - 200
                            user_storage["exchange"] = 200
                        else:
                            response.set_text(game.fields[user_storage["field_cellU"]] + '\n Поздравляю, 200 $ ваши')
                            user_storage["moneyU"] = user_storage["moneyU"] + 2 * user_storage["exchange"]
                            user_storage["exchange"] = 0

                    if user_storage["field_cellU"] == 5 | user_storage["field_cellU"] == 16 | user_storage[
                        "field_cellU"] == 36:
                        response.set_text(chances(user_storage, game))

                    if user_storage["field_cellU"] == 34:
                        response.set_text(game.fields[user_storage["field_cellU"]])
                        user_storage["go"] = True

                    user_storage["users_turns"] = False
                    return response, user_storage

                # Если ходит Алиса

            elif not user_storage["users_turn"]:
                backup_turn = user_storage
                if cube + user_storage["field_cellA"] > 40:
                    user_storage["moneyA"] = user_storage["moneyA"] + 200
                    user_storage["bankA"] = user_storage["bankA"] * 1.5
                    user_storage["field_cellA"] = user_storage["field_cellA"] + cube - 40

                if cube + user_storage["field_cellA"] < 40:
                    user_storage["field_cellA"] = user_storage["field_cellA"] + cube

                if user_storage["field_cellA"] == 2 | user_storage["field_cellA"] == 4 | user_storage[
                    "field_cellA"] == 5 | user_storage["field_cellA"] == 7 | user_storage["field_cellA"] == 9 | \
                        user_storage["field_cellA"] == 10 | user_storage["field_cellA"] == 12 | user_storage[
                    "field_cellA"] == 14 | user_storage["field_cellA"] == 15 | user_storage["field_cellA"] == 17 | \
                        user_storage["field_cellA"] == 19 | user_storage["field_cellA"] == 20 | user_storage[
                    "field_cellA"] == 22 | user_storage["field_cellA"] == 24 | user_storage["field_cellA"] == 25 | \
                        user_storage["field_cellA"] == 27 | user_storage["field_cellA"] == 28 | user_storage[
                    "field_cellA"] == 30 | user_storage["field_cellA"] == 32 | user_storage["field_cellA"] == 33 | \
                        user_storage["field_cellA"] == 35 | user_storage["field_cellA"] == 38 | user_storage[
                    "field_cellA"] == 40:

                    a = conversion(user_storage["field_cellA"])

                    b = randint(1, 2)

                    if user_storage["moneyA"] < 41:
                        b = 2

                    if user_storage["propertyU"][a] == 1:
                        response.set_text("Алиса попала на ваш участок: " + game.fields[user_storage["field_cellA"]])
                        user_storage["moneyA"] = user_storage["moneyA"] + game.price_field[user_storage["field_cellA"]]
                        user_storage["moneyU"] = user_storage["moneyU"] - game.price_field[user_storage["field_cellA"]]

                    else:
                        if b == 1:
                            response.set_text(
                                "Алиса попала: " + game.fields[user_storage["field_cellA"]] + " и решила купить")
                            user_storage["moneyA"] = user_storage["moneyA"] + game.price_field[
                                user_storage["field_cellA"]]
                            user_storage["propertyA"][a] = 1
                        else:
                            response.set_text(
                                "Алиса попала: " + game.fields[user_storage["field_cellA"]] + " и решила не покупать")

                if user_storage["field_cellA"] == 26 | user_storage["field_cellA"] == 21 | user_storage[
                    "field_cellA"] == 29 | user_storage["field_cellA"] == 39 | user_storage["field_cellA"] == 3 | \
                        user_storage[
                            "field_cellA"] == 8:
                    user_storage["moneyA"] = user_storage["moneyA"] + game.price_field[user_storage["field_cellA"]]
                    response.set_text(game.fields[user_storage["field_cellA"]])

                if user_storage["field_cellA"] == 23:
                    response.set_text('\n Алиса ' + game.fields[user_storage["field_cellA"]])
                    user_storage["moneyA"] = user_storage["moneyA"] + 200
                    user_storage["field_cellA"] = 1

                if user_storage["field_cellA"] == 31:
                    response.set_text('\n Алиса ' + game.fields[user_storage["field_cellA"]])
                    user_storage["moneyA"] = user_storage["moneyA"] + 100
                    user_storage["field_cellA"] = 11

                if user_storage["field_cellA"] == 6:
                    response.set_text(game.fields[user_storage["field_cellA"]])
                    user_storage["moneyA"] = user_storage["moneyA"] - 50
                    user_storage["moneyU"] = user_storage["moneyU"] + 50

                if user_storage["field_cellA"] == 37:
                    response.set_text(game.fields[user_storage["field_cellA"]])
                    user_storage["bank"] = True

                if user_storage["field_cellA"] == 1:
                    response.set_text('\n Алиса попала в ' + game.fields[user_storage["field_cellA"]])

                if user_storage["field_cellA"] == 11:
                    response.set_text('\n Алиса попала в ' + game.fields[user_storage["field_cellA"]])
                    user_storage["moneyA"] = user_storage["moneyA"] - 100

                if user_storage["field_cellA"] == 18:
                    response.set_text(game.fields[user_storage["field_cellA"]])
                    response.set_text(school(user_storage, game))

                if user_storage["field_cellA"] == 13:
                    if user_storage["exchange"] == 0:
                        response.set_text(game.fields[user_storage["field_cellA"]] + '\nАлиса оставила деньги на бирже')
                        user_storage["moneyA"] = user_storage["moneyA"] - 200
                        user_storage["exchange"] = 200
                    else:
                        response.set_text(game.fields[user_storage["field_cellA"]] + '\nАлиса взяла деньги с биржи')
                        user_storage["moneyA"] = user_storage["moneyA"] + 2 * user_storage["exchange"]
                        user_storage["exchange"] = 0

                if user_storage["field_cellA"] == 5 | user_storage["field_cellA"] == 16 | user_storage[
                    "field_cellA"] == 36:
                    response.set_text(chances(user_storage, game))

                if user_storage["field_cellA"] == 34:
                    field = randint(1, 40)
                    if user_storage["field_cellA"] > field:
                        user_storage["moneyA"] = user_storage["moneyA"] + 200
                    response.set_text(game.fields[user_storage["field_cellA"]] + " Выбор Алисы: " + game.fields[field])
                    user_storage["field_cellA"] = field
                user_storage["users_turns"] = True
                return response, user_storage

        else:
            response.set_text("Простите, но я вас не поняла.")
            return response, user_storage


# Шансы
def chances(user_storage, game):
    rand = randint(1, 12)
    if (rand == 1 | rand == 2 | rand == 4 | rand == 5 | rand == 6 | rand == 8 | rand == 9 | rand == 12) & user_storage[
        "users_turns"] == True:
        user_storage["moneyU"] = user_storage["moneyU"] + game.price_chance[rand]

    if (
            rand == 1 | rand == 2 | rand == 4 | rand == 5 | rand == 6 | rand == 8 | rand == 9 | rand == 12) & \
            user_storage["users_turns"] == False:
        user_storage["moneyA"] = user_storage["moneyA"] + game.price_chance[rand]

    if rand == 3 & user_storage["users_turns"] == True:
        user_storage["field_cellU"] = user_storage["field_cellU"] - 5

    if rand == 3 & user_storage["users_turns"] == False:
        user_storage["field_cellA"] = user_storage["field_cellA"] - 5

    if rand == 10 & user_storage["users_turns"] == True:
        user_storage["field_cellU"] = user_storage["field_cellU"] + 3

    if rand == 10 & user_storage["users_turns"] == False:
        user_storage["field_cellA"] = user_storage["field_cellA"] + 3

    if rand == 11 & user_storage["users_turns"] == True:
        user_storage["field_cellU"] = 11
        user_storage["moneyU"] = user_storage["moneyU"] - 100

    if rand == 11 & user_storage["users_turns"] == False:
        user_storage["field_cellA"] = 11
        user_storage["moneyA"] = user_storage["moneyA"] - 100

    if rand == 7 & user_storage["users_turns"] == True:
        user_storage["field_cellU"] = 21

    if rand == 7 & user_storage["users_turns"] == False:
        user_storage["field_cellA"] = 21

    if not user_storage["users_turns"]:
        return 'Алиса: ' + game.fields[user_storage["field_cellA"]] + game.chance[rand]

    if user_storage["users_turns"]:
        return game.fields[user_storage["field_cellA"]] + game.chance[rand]


# Начало новой игры
def end(request, response):
    game = las_vegas()

    user_storage = {
        "propertyA": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0],  # имущество Алисы
        "propertyU": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0],  # имущество пользователя
        "moneyU": 200,  # Деньги Пользователя
        "moneyA": 200,  # Деньги Алисы
        "field_cellA": 0,  # Клетка, на которой находится Алиса
        "field_cellU": 0,  # Клетка, на которой находится пользователь
        "bankU": 0,  # вклады пользователя (ячейка поля 37)
        "bankA": 0,  # вклады алисы (ячейка поля 37)
        "exchange": 0,  # биржа (ячейка поля 13)
        "user_id": request.user_id,
        "users_turn": True,
        "bank": False,
        "go": False,
        "property": 0,
        "school": 0
    }

    backup_turn = user_storage

    response.set_text('Давай напомню правила: Каждый участник бросает кубик и в зависимости от выпавшего количества '
                      'очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – '
                      'не обанкротиться. \n Если вы остановились на поле недвижимости и оно не '
                      'занято другими участниками, у вас есть право на его покупку или отказ от покупки. \n Владение зданием дает право взыскивать арендную плату с человека, '
                      'остановившегося на этом поле.\n «Тюрьма»: Чтобы покинуть этот сектор, необходимо заплатить '
                      'штраф в 100 $. \n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь '
                      'банкротом. \n \n Чтобы начать новую игру наберите "новая игра", чтобы сделать свой ход '
                      'наберите "бросить кубик"')

    return user_storage


def school(user_storage, game):
    rand = randint(1, 11)
    if not user_storage["users_turns"]:
        choise = randint(1, 2)
        if choise == 1:
            user_storage["moneyA"] = user_storage["moneyA"] + 50
            return (game.fields[18] + '\n' + game.questions[rand] + '\n Ответ Алисы:' + game.answers[
                rand] + '\nПравильный ответ')
        else:
            return game.fields[18] + '\n' + game.questions[rand] + '\n Ответ Алисы: я не знаю. НЕ засчитано'

    if user_storage["users_turns"]:
        user_storage["flag"] = rand
        return game.fields[18] + '\n' + game.questions[rand]


def conversion(a):
    if a == 2:
        a = 0
    if a == 4:
        a = 1
    if a == 7:
        a = 2
    if a == 9:
        a = 3
    if a == 10:
        a = 4
    if a == 12:
        a = 5
    if a == 14:
        a = 6
    if a == 15:
        a = 7
    if a == 17:
        a = 8
    if a == 19:
        a = 9
    if a == 20:
        a = 10
    if a == 22:
        a = 11
    if a == 24:
        a = 12
    if a == 25:
        a = 13
    if a == 27:
        a = 14
    if a == 28:
        a = 15
    if a == 30:
        a = 16
    if a == 32:
        a = 17
    if a == 33:
        a = 18
    if a == 38:
        a = 19
    if a == 40:
        a = 20
    return a
