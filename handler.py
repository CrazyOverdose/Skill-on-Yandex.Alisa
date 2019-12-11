from __future__ import unicode_literals

import logging
import random
from random import randint

logging.basicConfig(level=logging.DEBUG)


class WinnerError1(Exception):
    """Класс - исключение для победы Алисы"""
    pass


class WinnerError2(Exception):
    """Класс - исключение для победы пользователя"""
    pass


class Draw(Exception):
    """Класс - исключение для ничьи"""
    pass


class las_vegas:
    """Класс - поле игры
    Attributes:
        questions(list): Вопросы для клетки "Назад в школу"
        answers(list): Ответы для клетки "Назад в школу"
        fields(list): Описание всех клеток поля
        price_field(list): Цены всех ячеек поля
        price_foreign_field(list): Цены, которые заплатит тот, кто попал на чужую недвижимость """
    questions = ['0', 'Чему равно 2+4-3*2', 'Какое из чисел натуральное? 0, 4, 0.2, 1/2',
                 'Cтолица Канады (Соблюдайте правила русского языка, пожалуйста)',
                 'Столица Южной Кореи (Соблюдайте правила русского языка, пожалуйста)',
                 'На какую букву ударание в слове "щавель"',
                 'Какая буква пропущена? Параш..т',
                 'Кто написал "Горе от ума"? (Соблюдайте правила русского языка, пожалуйста)',
                 'Является ли банан фруктом?',
                 'Чему равна площадь треугольника со сторонами 4 на 3 на 5', 'Сколько в 1км сантиметров?',
                 'Сколько лет длилась Первая Мировая война?']

    answers = ['0', '0', '4', 'Оттава', 'Сеул', 'е', 'ю', 'Грибоедов', 'нет', '6', '100000', '4']

    fields = ['0', '\n 1. Cтарт \n', '\n 2. Колесо обозрения "High Roller" Цена: 10$ \n ',
              '\n 3. Инвестроры вложили в вас 100$\n',
              '\n 4. Ранчо "Casa de Shenandoah" Цена: 10$\n', '\n 5. Отправляйтесь на 2 ячейки назад\n',
              '\n 6. Брат за брата. Отдайте второму игроку 50$\n',
              '\n7. Плотина Гувера Цена: 20$\n', '\n 8. Какая жалость...у вас сломался холодильник -50$\n',
              '\n 9. Улица Фримонт-стрит Цена: 20$\n', '\n 10. Аллея Лас-Вегас Цена: 20$\n',
              '\n 11. Тюрьма. Вы пропускаете ход и теряете 150$\n',
              '\n 12. Парка развлечений "Adventuredome" Цена: 30$\n',
              '\n 13. Биржа. Если она пуста, то должен оставить 100$, если нет,то вправе забрать в 1.5 раза больше, '
              'чем на ней '
              'есть или оставить еще 100\n',
              '\n 14. Музей Shelby American Цена: 30$\n', '\n 15. Национальный музей атомных испытаний Цена: 30$\n',
              '\n 16. Отправляйтесь на биржу. Если биржа пуста, то должен оставить 100$, если нет,то вправе забрать в 1.5 '
              'раза больше, чем на ней '
              'есть или оставить еще 100\n',
              '\n 17. Музей Моб Цена: 40$\n',
              '\n 18. Назад в будущее. Игроку будет задан один школьный вопрос. За правильный ответ +50$\n',
              '\n 19. Отель-Казино "Белладжио" Цена: 40$\n', '\n20. Музей Неона Цена: 40$\n',
              '\n 21. Бесплатный ночлег\n',
              '\n 22. Развлекательный комплекс "Луксор Лас-Вегас" Цена: 45$\n', '\n 23. Отправляйтесь на начало\n',
              '\n 24. Отель-казино "Париж Лас-Вегас" Цена: 45$\n',
              '\n 25. Отель-казино "Венецианский Лас-Вегас" Цена: 45$\n',
              '\n 26. Мотель. Вы остановились переночевать в мотеле. Заплатите 100$\n',
              '\n 27. Отель-казино "Wynn" Цена: 50$\n',
              '\n 28. Развлекательный комплекс "Сизарс-Пэлас" Цена: 50$\n',
              '\n 29. Лотерея. Да вы везунчик, заберите свои законные 95$\n',
              '\n 30. Отель-казино "Стратосфера Лас-Вегас" Цена: 50$\n',
              '\n 31. Отправляйтесь в тюрьму\n', '\n 32. Часовня цветов Цена: 55$\n',
              '\n 33. Музей мадам Тюссо Цена: 55$\n',
              '\n 34. Выберете любую ячейку, на которую отправитесь.\n',
              '\n 35. Ред-Рок-Каньон Цена: 55$\n', '\n 36. Отправляйтесь на 3 ячейки вперед \n',
              '\n 37. Банк. Вы можете положить деньги под 10% за круг (скажите, сколько денег хотите положить), забрать ранее вложенные деньги (с процентами) Для этого скажите "забрать"\n',
              '\n 38. Национальный парк "Долина смерти" Цена: 60$\n',
              '\n 39. Вы такой невнимательный! Как умудрились потерять 50$?\n',
              '\n 40. Сансет Парк Цена: 60$\n']

    price_field = [0, 200, -10, 100, -10, 0, -50, -20, -50, -20, -20, -150, -30, 0, -30, -30, 0, -40, 0, -40, -40, 0,
                   -45, 200, -45, -45, -100, -50, -50, 95, -50, 0, -55, -55, 0, -55, 0, 0, -60, -50, -60]

    price_foreign_field = [0, 200, -30, 100, -30, 0, -50, -50, -50, -50, -50, -200, -70, 0, -70, -70, 0, -85, 0, -85,
                           -85, 0, -100, 200, -100, -100, -100, -120, -120, 95, -120, 0, -135, -135, 0, -135, 0, 0,
                           -150, -50, -150]


## Слова для показа количества денег Алисы и пользователя
MONEY = ['деньги', 'моиденьги', 'сколькоуменяденег', 'сколькоденег', 'финансы', 'сбережения']

## Слова для совершения хода Алисы или пользователя
WORDS = ['броситькубик', 'яхожу', 'го', 'давайиграть', 'играть', 'начать']

## Слова для начала новой игры
ENDING_WORDS = ['новаяигра', 'выход', 'начатьновуюигру']

## Слова для показа количества денег на бирже
BURSE = ['биржа', 'сколькоденегнабирже', 'деньгинабирже', 'деньгисбиржи']

## Слова для показа количества денег, вложенных в банк Алисой и пользователем
BANKS = ['банк', 'деньгивбанке', 'сколькоденегвбанке', 'вклады']

## Слова для того, чтобы забрать деньги с биржи или банка
BURSEtake = ['взять', 'забрать', 'взятьденьги', 'забратьденьги', ]

## Слова для того, чтобы оставить 100$ на бирже
BURSEgive = ['оставить', 'отдать', 'отдатьденьги', 'положить', 'оставитьденьги', 'положитьденьги', ]

## Слова, чтобы увидеть ячейку, где находится Алиса и пользователь
PLACE = ['мояячейка', 'гдея', 'где', 'моеположение', 'накакойяячейке', 'клетка', 'мояклетка', 'накакойяклетке']

## Слова для показа правил игры
RULES = ['правила', 'какиграть', 'описание', 'описаниеигры']

## Слова для вызова списка всех ячеек поля
MAP = ['ячейки', 'карта', 'поле', 'описаниеячеек']

## Слова для показа собственности Алисы и пользователя
OWN = ['недвижимость', 'моянедвижимость', 'собственность', 'мое', 'моё', 'моясобственность']


def handle_dialog(request, response, user_storage):
    """Функция обработки самой игры
    Args:
        request: Запрос пользователя
        response: Ответ пользователю
        user_storage: Состояние пользователя
    Returns:
        Ответ для пользователя и его хранилище"""

    ##Экземпляр поля
    game = las_vegas()
    random.seed()
    ## Обработка новой сессии
    if request.is_new_session:
        user_storage = {
            "propertyA": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # имущество Алисы
            "propertyU": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            # имущество пользователя
            "moneyU": 200,  # Деньги Пользователя
            "moneyA": 200,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0,  # деньги на бирже (ячейка поля 13)
            "user_id": request.user_id,
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": False,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        ## Приветствие пользователя
        response.set_text(
            'Добро пожаловать в "Лас-Вегас"! Ты пришёл почувствовать себя успешным предпринимателем!'
            'Каждый участник бросает кубик и в зависимости от выпавшего количества '
            'очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 100$. Ваша цель – '
            'не обанкротиться. \n Если вы остановились на поле недвижимости и оно не '
            'занято другими участниками, у вас есть право на его покупку или отказ от покупки. \n Владение зданием '
            'дает право взыскивать арендную плату с человека, '
            'остановившегося на этом поле.\n «Тюрьма»: Попав на эту ячейку, вы теряете 150$ и пропускаете ход'
            '\n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь '
            'банкротом. \n \n Чтобы начать игру "бросить кубик"')

        return response, user_storage

    ## Обработка запроса пользователя.
    user_message = request.command.lower().strip().replace(' ', '')

    try:
        ##Собственность Алисы и пользователя
        if user_message in OWN:
            text = 'Собственность Алисы: '
            for i in range(1, 23):
                if user_storage["propertyA"][i] == 1:
                    desipher = deconversion(i)
                    text = text + game.fields[desipher]

            text = text + '\nВаша собственность: '
            for j in range(1, 23):
                if user_storage["propertyU"][j] == 1:
                    desipher = deconversion(j)
                    text = text + game.fields[desipher]

            response.set_text(text)
            return response, user_storage

        ##Вывод денежного состояния Алисы и пользователя
        if user_message in MONEY:
            response.set_text(
                'Ваши деньги ' + str(user_storage["moneyU"]) + ' $\nДеньги Алисы ' + str(user_storage["moneyA"]) + ' $')
            return response, user_storage

        ##Вывод всех ячеек поля
        if user_message in MAP:
            response.set_text(
                '1 - Cтарт\n2 - Колесо обозрения "High Roller"\n3 - Лучший предприниматель\n'
                '4 - Ранчо "Casa de Shenandoah"\n5 - Идите на 2 ячейки назад\n6 - Брат за брата\n'
                '7 - Плотина Гувера\n 8 - Сломанный холодильник\n'
                '9 - Улица Фримонт-стрит\n 10 - Аллея Лас-Вегас\n 11 - Тюрьма'
                '\n 12 - Парка развлечений "Adventuredome"\n'
                '13 - Биржа\n'
                '14 - Музей Shelby American\n 15 - Музей атомных испытаний\n 16 - Отправляйтесь на биржу \n'
                '17 - Музей Моб\n '
                '18 - Назад в будущее\n'
                '19 - Отель-Казино "Белладжио"\n20 - Музей Неона\n  21 - Бесплатный ночлег\n'
                '22 - Развлекательный комплекс "Луксор Лас-Вегас"\n 23 - Отправляйтесь на начало\n'
                '24 - Отель-казино "Париж Лас-Вегас"\n25 - Отель-казино "Венецианский Лас-Вегас"\n'
                '26 - Мотель\n 27 - Отель-казино "Wynn"\n'
                '28 - Развлекательный комплекс "Сизарс-Пэлас"\n'
                '29 - Лотерея\n 30 - Отель-казино "Стратосфера Лас-Вегас"\n'
                '31 - Отправляйтесь в тюрьму\n 32 - Часовня цветов\n 33 - Музей мадам Тюссо\n'
                '34 - Любая ячейка.\n'
                '35 - Ред-Рок-Каньон\n 36 - Идите на 3 ячейки вперед \n'
                '37 - Банк\n'
                '38 - Национальный парк "Долина смерти"\n 39 - Потеря\n'
                '40 - Сансет Парк')
            return response, user_storage

        ##Вывод количества денег на бирже
        if user_message in BURSE:
            response.set_text('Сейчас на бирже ' + str(user_storage["exchange"]) + ' $')
            return response, user_storage

        ##Вывод количества денег, вложенных Алисой и пользователем в банк
        if user_message in BANKS:
            response.set_text(
                'Вклады Алисы: ' + str(user_storage["bankA"]) + ' $\n Ваши вклады ' + str(user_storage["bankU"]) + ' $')
            return response, user_storage

        ##Вывод ячеек, на которых находятся Алиса и пользователь
        if user_message in PLACE:
            response.set_text('Вы находитесь на ' + user_storage["field_cellU"] + ' ячейке \n Алиса на ' + user_storage[
                "field_cellA"])
            return response, user_storage

        ##Обработка начала новой игры
        if user_message in ENDING_WORDS:
            text = ''
            user_storage = end(request, response, text)
            return response, user_storage

        ##Вывод правил игры
        if user_message in RULES:
            response.set_text('Каждый участник бросает кубик и в зависимости от выпавшего количества '
                              'очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. '
                              'Ваша цель – '
                              'не обанкротиться. \n Если вы остановились на поле недвижимости и оно не '
                              'занято другими участниками, у вас есть право на его покупку или отказ от покупки. '
                              '\n Владение зданием '
                              'дает право взыскивать арендную плату с человека, '
                              'остановившегося на этом поле.\n «Тюрьма»: Попав на эту ячейку, вы теряете 150$ и '
                              'пропускаете ход '
                              '\n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь '
                              'банкротом. \n \n Чтобы начать игру "бросить кубик"')
            return response, user_storage

        if user_storage["school"] != 0:
            ##Пользователь попал на ячейку "Назад в школу". Обработка ячейки
            if str(user_message) == game.answers[user_storage["school"]]:
                response.set_text('Правильный ответ')
                user_storage["moneyU"] = user_storage["moneyU"] + 50
            else:
                response.set_text('Неправильный ответ \n Правильный ответ: ' + game.answers[user_storage["school"]])
            user_storage["school"] = 0
            return response, user_storage

        if user_storage["choice"]:
            ##Обработка попадания пользователя на биржу
            if user_message in BURSEtake:
                user_storage["moneyU"] = user_storage["moneyU"] + user_storage["exchange"] * 1.5
                response.set_text('Вы взяли ' + str(user_storage["exchange"] * 1.5) + ' $ с биржи')
                user_storage["exchange"] = 0

            if user_message in BURSEgive:
                user_storage["moneyU"] = user_storage["moneyU"] - 100
                user_storage["exchange"] = user_storage["exchange"] + 100
                response.set_text('Вы оставили 100$ на бирже')

            if user_message not in BURSEgive + BURSEtake:
                response.set_text('Иногда ничего не делать - лучшее решение')
            user_storage["choice"] = False
            return response, user_storage

        ##Если Алиса и пользователь оказались в тюрьме одновременно
        if user_storage["prison1"] and user_storage["prison2"]:
            user_storage["users_turn"] = True
            user_storage["prison1"] = False
            user_storage["prison2"] = False
            response.set_text('Алиса помогла сбежать вам из тюрьмы, ходите ')
            return response, user_storage

        ##Алиса попала в тюрьму и пропускает ход
        if user_storage["prison1"]:
            if not user_storage["users_turn"]:
                user_storage["users_turn"] = True
                user_storage["prison1"] = False

        ##Пользователь попал в тюрьму и пропускает ход
        if user_storage["prison2"]:
            if user_storage["users_turn"]:
                user_storage["users_turn"] = False
                user_storage["prison2"] = False

        ##Обработка ячейки для пользователя "перемещение на любую ячейку"
        if user_storage["go"]:
            if user_message.isdigit():
                response.set_text(
                    '\n Вы перешли на ячейку ' + str(user_message) + '\n' + game.fields[user_message])
                if user_storage["field_cellU"] + int(user_message) < 40:
                    user_storage["moneyU"] = user_storage["moneyU"] + 200
                user_storage["field_cellU"] = int(user_message)
                user_storage["anycell2"] = True
            if not user_message.isdigit():
                response.set_text('Ваш ход \n' + '\n Вы остались на месте ')
            user_storage["go"] = False
            return response, user_storage

        ##Обработка попадания пользователя в банк
        if user_storage["bank"]:

            if user_message in BURSEtake:
                if user_storage["bankU"] == 0:
                    response.set_text('Ваши вклады пусты, вам нечего забирать')
                else:
                    user_storage["moneyU"] = user_storage["moneyU"] + user_storage["bankU"]
                    response.set_text('Вы обналичили ' + str(user_storage["bankU"]) + ' $ ')
                    user_storage["bankU"] = 0

            if user_message.isdigit():
                if float(user_message) > user_storage["moneyU"]:
                    response.set_text('Нехорошо врать, у тебя нет столько денег')
                else:
                    user_storage["bankU"] = user_storage["bankU"] + float(user_message)
                    user_storage["moneyU"] = user_storage["moneyU"] - float(user_message)
                    response.set_text('Вы оставили ' + str(user_message) + ' $ в банке')
            if user_message.isdigit() == False and user_message not in BURSEtake:
                response.set_text('Денюжки греют душу,когда они под рукой, не так ли?')
            user_storage["bank"] = False
            return response, user_storage

        ##ОБработка решения пользователя насчет недвижимости (купить, не купить)
        if user_storage["property"] != 0:
            if str(user_message) == 'купить':
                if user_storage["moneyU"] < game.price_field[user_storage["field_cellU"]]:
                    response.set_text('У вас недостаточно средств ')
                else:
                    user_storage["moneyU"] = user_storage["moneyU"] + game.price_field[user_storage["field_cellU"]]
                    user_storage["propertyU"][user_storage["property"]] = 1
                    response.set_text('Поздравляю с приобретением! ')
            else:
                response.set_text('Может, это действительно не лучшее вложение денег')
            user_storage["property"] = 0
            return response, user_storage

        ##Продажа недвижимости Алисы, когда она на грани банкротства
        if not user_storage["users_turn"]:
            if user_storage["moneyA"] <= 0:
                flag = 0
                for i in range(1, 23):
                    if user_storage["propertyA"][i] == 1:
                        flag = i
                        break
                if flag != 0:
                    i = deconversion(flag)
                    response.set_text('Алиса продала свою недвижимость ' + game.fields[i] + ' за ' + str(abs(game.price_field[i] // 2)) + ' $')
                    user_storage["moneyA"] = user_storage["moneyA"] - (game.price_field[i] // 2)
                    user_storage["propertyA"][flag] = 0
                    user_storage["users_turn"] = True
                    return response, user_storage

        ##Продажа недвижимости пользователя, когда он на грани банкротства
        if user_storage["users_turn"]:
            if user_storage["moneyU"] <= 0:
                flag = 0
                for j in range(1, 23):
                    if int(user_storage["propertyU"][int(j)]) == 1:
                        flag = j
                        break
                if flag != 0:
                    if not user_storage["crash"]:
                        response.set_text(
                            'Вы находитесь на грани банкротства, скажите, какую недвижимость хотите продать? ')
                        user_storage["crash"] = True
                        return response, user_storage
                    if user_storage["crash"]:
                        if user_message.isdigit():
                            if int(user_message) == 2 or int(user_message) == 4 or int(user_message) == 5 or int(
                                    user_message) == 7 or int(user_message) == 9 or int(user_message) == 10 or int(
                                user_message) == 12 or int(user_message) == 14 or int(user_message) == 15 or int(
                                user_message) == 17 or int(user_message) == 19 or int(user_message) == 20 or int(
                                user_message) == 22 or int(user_message) == 24 or int(user_message) == 25 or int(
                                user_message) == 27 or int(user_message) == 28 or int(user_message) == 30 or int(
                                user_message) == 32 or int(user_message) == 33 or int(user_message) == 35 or int(
                                user_message) == 38 or int(user_message) == 40:
                                if user_storage["propertyU"][conversion(int(user_message))] == 1:
                                    response.set_text(
                                        'Вы продали свою недвижимость ' + game.fields[int(user_message)] + ' за ' + str(
                                            abs(game.price_field[int(user_message)] // 2)) + ' $')
                                    user_storage["moneyU"] = user_storage["moneyU"] - (
                                                game.price_field[int(user_message)] // 2)
                                    user_storage["propertyU"][conversion(int(user_message))] = 0
                                    user_storage["crash"] = False
                                    user_storage["users_turn"] = False
                                    return response, user_storage
                                else:
                                    response.set_text('Вы не владеете данным имуществом')
                                    return response, user_storage
                            else:
                                response.set_text('Зачем вы ввели номер несуществующей ячейки недвижимости?')
                                return response, user_storage
                        else:
                            response.set_text('Вы не ввели номер ячейки недвижимости')
                            return response, user_storage

        ##Выпадение исключения в случае ничьи
        if user_storage["moneyU"] < 0 and user_storage["moneyA"] < 0:
            raise Draw

        ##Выпадение исключения в случае банкротства пользователя
        if user_storage["users_turn"]:
            if user_storage["moneyU"] < 0:
                raise WinnerError1
        ##Выпадение исключения в случае банкротства Алисы
        if not user_storage["users_turn"]:
            if user_storage["moneyA"] < 0:
                raise WinnerError2

        ##Обработка самого хода Алисы или пользователя
        if user_message in WORDS:

            random.seed()
            ##Бросок кубика
            cube = 0

            ##Нарушение очередности хода для Алисы из-за ячейки 34 (переход на любую ячейку)
            if user_storage["anycell1"]:
                if user_storage["users_turn"]:
                    user_storage["users_turn"] = False
                    cube = 0
                    user_storage["anycell1"] = False
            ##Нарушение очередности хода для пользователя из-за ячейки 34 (переход на любую ячейку)
            if user_storage["anycell2"]:
                if not user_storage["users_turn"]:
                    user_storage["users_turn"] = True
                    cube = 0
                    user_storage["anycell2"] = False

            ##ОБРАБОТКА ХОДА АЛИСЫ
            if not user_storage["users_turn"]:
                ##Обработка броска кубика
                if cube + user_storage["field_cellA"] > 40:
                    user_storage["moneyA"] = user_storage["moneyA"] + 200
                    user_storage["bankA"] = user_storage["bankA"] + (user_storage["bankA"] // 100 * 10)
                    user_storage["field_cellA"] = user_storage["field_cellA"] + cube - 40

                else:
                    user_storage["field_cellA"] = user_storage["field_cellA"] + cube

                ##Отправляйтесь в начало
                if user_storage["field_cellA"] == 23:
                    response.set_text('Ход Алисы \n' + game.fields[user_storage["field_cellA"]])
                    user_storage["moneyA"] = user_storage["moneyA"] + 200
                    user_storage["field_cellA"] = 1
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##Обработка ячеек простого уменьшения/увеличения денег
                if int(user_storage["field_cellA"]) == 26 or int(user_storage["field_cellA"]) == 21 or int(
                        user_storage["field_cellA"]) == 29 or int(user_storage["field_cellA"]) == 39 or int(
                    user_storage["field_cellA"]) == 3 or int(user_storage["field_cellA"]) == 8:
                    user_storage["moneyA"] = user_storage["moneyA"] + game.price_field[user_storage["field_cellA"]]
                    response.set_text('Ход Алисы \n' + game.fields[user_storage["field_cellA"]])
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##Отправляйтесь в тюрьму
                if user_storage["field_cellA"] == 31:
                    response.set_text(
                        'Ход Алисы \n' + game.fields[user_storage["field_cellA"]] + game.fields[11])
                    user_storage["moneyA"] = user_storage["moneyA"] + 50
                    user_storage["field_cellA"] = 11
                    user_storage["prison1"] = True
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##Тюрьма
                if user_storage["field_cellA"] == 11:
                    user_storage["moneyA"] = user_storage["moneyA"] + game.price_field[user_storage["field_cellA"]]
                    response.set_text('Ход Алисы \n' + game.fields[user_storage["field_cellA"]])
                    user_storage["prison1"] = True
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##Брат за брата
                if user_storage["field_cellA"] == 6:
                    response.set_text('Ход Алисы \n' + game.fields[user_storage["field_cellA"]])
                    user_storage["moneyA"] = user_storage["moneyA"] - 50
                    user_storage["moneyU"] = user_storage["moneyU"] + 50
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##На две ячейки назад
                if user_storage["field_cellA"] == 5:
                    response.set_text(
                        'Ход Алисы \n' + game.fields[user_storage["field_cellA"]]) + '\n Алиса попала на ' + game.fields[user_storage["field_cellA"] - 2]
                    user_storage["field_cellA"] = 3
                    user_storage["moneyA"] = user_storage["moneyA"] + game.price_field[user_storage["field_cellA"]]
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##На 3 ячейки вперед
                if user_storage["field_cellA"] == 36:
                    response.set_text(
                        'Ход Алисы \n' + game.fields[user_storage["field_cellA"]] + '\n Алиса попала на ' + game.fields[
                            user_storage["field_cellA"] + 3])
                    user_storage["field_cellA"] = 39
                    user_storage["moneyA"] = user_storage["moneyA"] + game.price_field[user_storage["field_cellA"]]
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##Старт
                if user_storage["field_cellA"] == 1:
                    response.set_text('Ход Алисы \n' + game.fields[user_storage["field_cellA"]])
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##Недвижимость
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

                    k = 1
                    flag = 0
                    for j in range(1, 23):
                        if int(user_storage["propertyA"][int(j)]) == 1:
                            flag = flag + 1
                    j = 1
                    for j in range(1, 23):
                        if int(user_storage["propertyU"][int(j)]) == 1:
                            flag = flag + 1
                    if flag == 22:
                        k = 3

                    a = conversion(user_storage["field_cellA"])

                    b = randint(1, 2)

                    if user_storage["moneyA"] + game.price_field[user_storage["field_cellA"]] < 70:
                        b = 2

                    if user_storage["propertyU"][a] == 1:
                        response.set_text('Ход Алисы \n' + 'Алиса попала на ваш участок: ' + game.fields[
                            user_storage["field_cellA"]] + 'и заплатила ' + str(abs(game.price_foreign_field[
                                                                                        user_storage[
                                                                                            "field_cellA"]] * k)) + '$\n' + '\n Если скуплены все ячейки недвижимости, стоимость попадания на них возрастает в 3 раза')
                        user_storage["moneyA"] = user_storage["moneyA"] + (
                                    game.price_foreign_field[user_storage["field_cellA"]] * k)
                        user_storage["moneyU"] = user_storage["moneyU"] - (
                                    game.price_foreign_field[user_storage["field_cellA"]] * k)

                    if user_storage["propertyA"][a] == 1:
                        response.set_text('Ход Алисы \n' +
                                          'Алиса попала на свою территорию: ' + game.fields[
                                              user_storage["field_cellA"]])

                    if user_storage["propertyA"][a] == 0 and user_storage["propertyU"][a] == 0:
                        if b == 1:
                            response.set_text('Ход Алисы \n' + game.fields[user_storage[
                                "field_cellA"]] + ' и решила купить \n Если вы попадете на данный сектор, то заплатите ' + str(
                                abs(game.price_foreign_field[user_storage[
                                    "field_cellA"]])) + ' $' + '\n Если скуплены все ячейки недвижимости, стоимость попадания на них возрастает в 3 раза')
                            user_storage["moneyA"] = user_storage["moneyA"] + game.price_field[
                                user_storage["field_cellA"]]
                            user_storage["propertyA"][a] = 1
                        else:
                            response.set_text('Ход Алисы \n' +
                                              'Алиса попала: ' + game.fields[
                                                  user_storage["field_cellA"]] + ' и решила не покупать')
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##Биржа
                if user_storage["field_cellA"] == 13 or user_storage["field_cellA"] == 16:
                    y = randint(1, 2)

                    rialto = user_storage["exchange"]

                    if rialto == 0:
                        response.set_text('Ход Алисы \n' + game.fields[
                            user_storage["field_cellA"]] + '\nАлиса оставила деньги на бирже')
                        user_storage["moneyA"] = user_storage["moneyA"] - 100
                        user_storage["exchange"] = 100

                    if rialto != 0:

                        if user_storage["moneyA"] < 150:
                            y = 2

                        if y == 2:
                            response.set_text('Ход Алисы \n' + game.fields[
                                user_storage["field_cellA"]] + '\nАлиса взяла деньги с биржи')
                            user_storage["moneyA"] = user_storage["moneyA"] + 1.5 * user_storage["exchange"]
                            user_storage["exchange"] = 0

                        if y == 1:
                            response.set_text('Ход Алисы \n' + game.fields[
                                user_storage["field_cellA"]] + '\nАлиса оставила деньги на бирже')
                            user_storage["moneyA"] = user_storage["moneyA"] - 100
                            user_storage["exchange"] = user_storage["exchange"] + 100
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##Банк
                if user_storage["field_cellA"] == 37:
                    y = randint(1, 3)

                    if user_storage["moneyA"] < 100 and user_storage["bankA"] == 0:
                        y = 2

                    if user_storage["bankA"] == 0:
                        y = randint(1, 2)

                    if user_storage["moneyA"] < 100:
                        y = randint(2, 3)

                    if y == 2:
                        response.set_text('Ход Алисы \n' + game.fields[
                            user_storage["field_cellA"]] + '\nАлиса оставила денюжки у себя')

                    if y == 1:
                        money = randint(user_storage["moneyA"] // 5, user_storage["moneyA"] // 2)
                        user_storage["bankA"] = user_storage["bankA"] + money
                        user_storage["moneyA"] = user_storage["moneyA"] - money
                        response.set_text(
                            'Ход Алисы \n' + game.fields[user_storage["field_cellA"]] + '\nАлиса оставила ' + str(
                                money) + ' $ в банке')

                    if y == 3:
                        user_storage["moneyA"] = user_storage["moneyA"] + user_storage["bankA"]
                        response.set_text('Ход Алисы \n' + game.fields[
                            user_storage["field_cellA"]] + '\nАлиса обналичила свой счёт в банке на сумму ' + str(
                            user_storage["bankA"]) + ' $ ')
                        user_storage["bankA"] = 0
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##Назад в школу
                if user_storage["field_cellA"] == 18:
                    rand = randint(1, 11)
                    choise = randint(1, 2)
                    if choise == 1:
                        user_storage["moneyA"] = user_storage["moneyA"] + 50
                        response.set_text(
                            'Ход Алисы \n ' + game.fields[18] + '\n' + game.questions[rand] + '\n Ответ Алисы:' +
                            game.answers[rand] + '\nПравильный ответ')
                    else:
                        response.set_text('Ход Алисы \n ' + game.fields[18] + '\n' + game.questions[
                            rand] + '\n Ответ Алисы: я не знаю. Нe засчитано')
                    user_storage["users_turn"] = True
                    return response, user_storage

                ##Перемещение на любую ячейку
                if user_storage["field_cellA"] == 34:
                    cell = randint(1, 40)

                    if cell + user_storage["field_cellA"] > 40:
                        user_storage["moneyA"] = user_storage["moneyA"] + 200
                        cell = cell + user_storage["field_cellA"] - 40
                    if cell + user_storage["field_cellA"] < 40:
                        cell = cell + user_storage["field_cellA"]

                    response.set_text(
                        'Ход Алисы \n' + game.fields[user_storage["field_cellA"]] + '\n Алиса перешла на ячейку ' + str(
                            cell))
                    user_storage["field_cellA"] = cell
                    user_storage["anycell1"] = True

                user_storage["users_turn"] = True
                return response, user_storage

            ##ХОД ПОЛЬЗОВАТЕЛЯ
            if user_storage["users_turn"]:
                ##Бросок кубика
                if cube + user_storage["field_cellU"] > 40:
                    user_storage["moneyU"] = user_storage["moneyU"] + 200
                    user_storage["bankU"] = user_storage["bankU"] + (user_storage["bankU"] // 100 * 10)
                    user_storage["field_cellU"] = user_storage["field_cellU"] + cube - 40

                else:
                    user_storage["field_cellU"] = user_storage["field_cellU"] + cube

                ##Отправляйтесь в начало
                if user_storage["field_cellU"] == 23:
                    response.set_text('Ваш ход \n' + game.fields[user_storage["field_cellU"]])
                    user_storage["moneyU"] = user_storage["moneyU"] + 200
                    user_storage["field_cellU"] = 1
                    user_storage["users_turn"] = False
                    return response, user_storage

                ##На две ячейки назад
                if user_storage["field_cellU"] == 5:
                    response.set_text(
                        'Ваш ход \n' + game.fields[user_storage["field_cellU"]] + '\n Вы попали на ' + game.fields[
                            user_storage["field_cellU"] - 2])
                    user_storage["field_cellU"] = 3
                    user_storage["moneyU"] = user_storage["moneyU"] + game.price_field[user_storage["field_cellU"]]
                    user_storage["users_turn"] = False
                    return response, user_storage

                ##На три ячейки вперед
                if user_storage["field_cellU"] == 36:
                    response.set_text(
                        'Ваш ход \n' + game.fields[user_storage["field_cellU"]] + '\n Вы попали на ' + game.fields[
                            user_storage["field_cellU"] + 3])
                    user_storage["field_cellU"] = 39
                    user_storage["moneyU"] = user_storage["moneyU"] + game.price_field[user_storage["field_cellU"]]
                    user_storage["users_turn"] = False
                    return response, user_storage

                ## Обработка простых уменьшений/увеличений состояния пользователя
                if int(user_storage["field_cellU"]) == 26 or int(user_storage["field_cellU"]) == 21 or int(
                        user_storage["field_cellU"]) == 29 or int(user_storage["field_cellU"]) == 39 or int(
                    user_storage["field_cellU"]) == 3 or int(user_storage["field_cellU"]) == 8:
                    user_storage["moneyU"] = user_storage["moneyU"] + game.price_field[user_storage["field_cellU"]]
                    response.set_text('Ваш ход \n' + game.fields[user_storage["field_cellU"]])
                    user_storage["users_turn"] = False
                    return response, user_storage

                ## Отправляйтесь в тюрьму
                if user_storage["field_cellU"] == 31:
                    response.set_text(
                        'Ваш ход \n' + game.fields[user_storage["field_cellU"]] + game.fields[11])
                    user_storage["moneyU"] = user_storage["moneyU"] + 50
                    user_storage["field_cellU"] = 11
                    user_storage["prison2"] = True
                    user_storage["users_turn"] = False
                    return response, user_storage

                ##Тюрьма
                if user_storage["field_cellU"] == 11:
                    user_storage["moneyU"] = user_storage["moneyU"] + game.price_field[user_storage["field_cellU"]]
                    response.set_text('Ваш ход \n' + game.fields[user_storage["field_cellU"]])
                    user_storage["prison2"] = True
                    user_storage["users_turn"] = False
                    return response, user_storage

                ##Брат за брата
                if user_storage["field_cellU"] == 6:
                    response.set_text('Ваш ход \n' + game.fields[user_storage["field_cellU"]])
                    user_storage["moneyU"] = user_storage["moneyU"] - 50
                    user_storage["moneyA"] = user_storage["moneyA"] + 50
                    user_storage["users_turn"] = False
                    return response, user_storage

                ##Старт
                if user_storage["field_cellU"] == 1:
                    response.set_text('Ваш ход \n' + game.fields[user_storage["field_cellU"]])
                    user_storage["users_turn"] = False
                    return response, user_storage

                ##Недвижимость
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

                    k = 1
                    flag = 0
                    for j in range(1, 23):
                        if user_storage["propertyA"][j] == 1:
                            flag = flag + 1
                    for j in range(1, 23):
                        if user_storage["propertyU"][j] == 1:
                            flag = flag + 1
                    if flag == 22:
                        k = 3

                    a = conversion(user_storage["field_cellU"])
                    if user_storage["propertyA"][a] == 1:
                        response.set_text('Ваш ход \n' + game.fields[user_storage[
                            "field_cellU"]] + ' \n Если скуплены все ячейки недвижимости, стоимость попадания на них возрастает в 3 раза \n Вы попали на недвижимость Алисы и заплатили ' + str(
                            abs(game.price_foreign_field[user_storage["field_cellU"]] * k)) + '$\n')
                        user_storage["moneyU"] = user_storage["moneyU"] + game.price_foreign_field[
                            user_storage["field_cellU"]] * k
                        user_storage["moneyA"] = user_storage["moneyA"] - game.price_foreign_field[
                            user_storage["field_cellU"]] * k

                    if user_storage["propertyU"][a] == 1:
                        response.set_text(
                            'Ваш ход \n' + game.fields[user_storage["field_cellU"]] + ' \nВы попали на свою территорию')

                    if user_storage["propertyU"][a] == 0 and user_storage["propertyA"][a] == 0:
                        response.set_text('Ваш ход \n' + game.fields[user_storage[
                            "field_cellU"]] + '\n Если Алиса попадет на эту недвижимость, она заплатит ' + str(abs(
                            game.price_foreign_field[user_storage[
                                "field_cellU"]])) + ' $  \n Если скуплены все ячейки недвижимости, стоимость попадания на них возрастает в 3 раза\n Чтобы приобрести: введите "купить"')
                        user_storage["property"] = a
                    user_storage["users_turn"] = False
                    return response, user_storage

                ##Биржа
                if user_storage["field_cellU"] == 13 or user_storage["field_cellU"] == 16:
                    if user_storage["exchange"] != 0:
                        response.set_text('Ваш ход \n' + game.fields[user_storage["field_cellU"]])
                        user_storage["choice"] = True

                    if user_storage["exchange"] == 0:
                        response.set_text('Ваш ход \n' + game.fields[
                            user_storage["field_cellU"]] + '\n Биржа пуста, вы оставили деньги')
                        user_storage["moneyU"] = user_storage["moneyU"] - 100
                        user_storage["exchange"] = 100
                    user_storage["users_turn"] = False
                    return response, user_storage

                ##Назад в школу
                if user_storage["field_cellU"] == 18:
                    rand = randint(1, 11)
                    user_storage["school"] = rand
                    response.set_text(game.fields[18] + '\n' + game.questions[rand])
                    user_storage["users_turn"] = False
                    return response, user_storage

                ##Переход на любую ячейку
                if user_storage["field_cellU"] == 34:
                    user_storage["go"] = True
                    response.set_text('Ваш ход \n' + game.fields[user_storage["field_cellU"]])
                    user_storage["users_turn"] = False
                    return response, user_storage

                ##Банк
                if user_storage["field_cellU"] == 37:
                    user_storage["bank"] = True
                    response.set_text('Ваш ход \n' + game.fields[user_storage["field_cellU"]])
                    user_storage["users_turn"] = False
                    return response, user_storage

                user_storage["users_turn"] = False
                return response, user_storage

        ## Если пользователь ввел какой-то неизвестный запрос
        else:
            response.set_text("Простите, но я вас не поняла.")

    ##Исключение - пользователь проиграл
    except WinnerError1:
        text = 'Мне очень жаль, но вы проиграли \n'
        user_storage = end(request, response, text)
    ##ИСключние - Алиса проиграла
    except WinnerError2:
        text = 'Поздравляю, вы победили! \n '
        user_storage = end(request, response, text)

    ##Исключение - ничья
    except Draw:
        text = 'Победила дружба :3 \n '
        user_storage = end(request, response, text)

    # В любом случае
    return response, user_storage


def end(request, response, text):
    """Начало новой игры
    Args:
        request: Запрос пользователя
        response: Ответ пользователю
        text: Добавляется к ответу для пользователя в случае завершения игры (победа, ничья, поражение)
    Returns:
        Хранилище пользователя"""
    response.set_text(text +
                      'Давай напомню правила: Каждый участник бросает кубик и в зависимости от выпавшего количества '
                      'очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – '
                      'не обанкротиться. \n Если вы остановились на поле недвижимости и оно не '
                      'занято другими участниками, у вас есть право на его покупку или отказ от покупки. \n Владение '
                      'зданием '
                      'дает право взыскивать арендную плату с человека, '
                      'остановившегося на этом поле.\n «Тюрьма»: Попав на эту ячейку, вы теряете 150$ и пропускаете '
                      'ход '
                      '\n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь '
                      'банкротом. \n \n Чтобы начать игру "бросить кубик"')

    user_storage = {
        "propertyA": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # имущество Алисы
        "propertyU": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # имущество пользователя
        "moneyU": 200,  # Деньги Пользователя
        "moneyA": 200,  # Деньги Алисы
        "field_cellA": 0,  # Клетка, на которой находится Алиса
        "field_cellU": 0,  # Клетка, на которой находится пользователь
        "bankU": 0,  # вклады пользователя (ячейка поля 37)
        "bankA": 0,  # вклады алисы (ячейка поля 37)
        "exchange": 0,  # деньги на бирже (ячейка поля 13)
        "user_id": request.user_id,
        "users_turn": True,  # чей ход
        "bank": False,  # пользователь попал в банк
        "property": 0,  # пользователь попал на ячейку недвижимости
        "go": False,  # на любую ячейку
        "school": 0,  # пользователь попал на "назад в школу"
        "choice": False,  # пользователь попал на биржу
        "prison1": False,  # тюрьма Алисы
        "prison2": False,  # тюрьма пользователя
        "crash": False,  # если пользователь почти банкрот
        "anycell1": False,
        "anycell2": False
    }

    return user_storage


def conversion(a):
    """Конвертация ячейки на поле в ячейку собственности
    Args:
          a(int): Ячейка, на которую попал пользователь/Алиса
    Returns:
          Номер ячейки недвижимости Алисы/пользователя"""
    if a == 2:
        a = 1
        return int(a)
    if a == 4:
        a = 2
        return int(a)
    if a == 7:
        a = 3
        return int(a)
    if a == 9:
        a = 4
        return int(a)
    if a == 10:
        a = 5
        return int(a)
    if a == 12:
        a = 6
        return int(a)
    if a == 14:
        a = 7
        return int(a)
    if a == 15:
        a = 8
        return int(a)
    if a == 17:
        a = 9
        return int(a)
    if a == 19:
        a = 10
        return int(a)
    if a == 20:
        a = 11
        return int(a)
    if a == 22:
        a = 12
        return int(a)
    if a == 24:
        a = 13
        return int(a)
    if a == 25:
        a = 14
        return int(a)
    if a == 27:
        a = 15
        return int(a)
    if a == 28:
        a = 16
        return int(a)
    if a == 30:
        a = 17
        return int(a)
    if a == 32:
        a = 18
        return int(a)
    if a == 33:
        a = 19
        return int(a)
    if a == 35:
        a = 20
        return int(a)
    if a == 38:
        a = 21
        return int(a)
    if a == 40:
        a = 22

    return int(a)


def deconversion(a):
    """Конвертация ячейки на поле в ячейку собственности
        Args:
              a(int): Ячейка недвижимости Алисы/пользователя
        Returns:
              Ячейка, на которую попал пользователь/Алиса"""
    if a == 1:
        a = 2
        return int(a)
    if a == 2:
        a = 4
        return int(a)
    if a == 3:
        a = 7
        return int(a)
    if a == 4:
        a = 9
        return int(a)
    if a == 5:
        a = 10
        return int(a)
    if a == 6:
        a = 12
        return int(a)
    if a == 7:
        a = 14
        return int(a)
    if a == 8:
        a = 15
        return int(a)
    if a == 9:
        a = 17
        return int(a)
    if a == 10:
        a = 19
        return int(a)
    if a == 11:
        a = 20
        return int(a)
    if a == 12:
        a = 22
        return int(a)
    if a == 13:
        a = 24
        return int(a)
    if a == 14:
        a = 25
        return int(a)
    if a == 15:
        a = 27
        return int(a)
    if a == 16:
        a = 28
        return int(a)
    if a == 17:
        a = 30
        return int(a)
    if a == 18:
        a = 32
        return int(a)
    if a == 19:
        a = 33
        return int(a)
    if a == 20:
        a = 35
        return int(a)
    if a == 21:
        a = 38
        return int(a)
    if a == 22:
        a = 40
    return int(a)
