from __future__ import unicode_literals
from json import dump
from random import randint, choice
from copy import deepcopy
from re import findall, match
import logging
import random

logging.basicConfig(level=logging.DEBUG)


class NoCellsError(Exception):
    pass


def handle_dialog(request, response, user_storage):
    if request.is_new_session:
        user_storage = {
            "user_id": request.user_id,
            "users_turn": True,
            "last_turn": None,
        }
        response.set.text(
            'Привет! Ты пришёл почувствовать себя успешным предпринимателем! Рассказать тебе правила игры "Лас-Вегас"?')
        return response, user_storage

    end = 17
    while end > 0:
        answers = request.command.lower().strip().replace(' ', '')
        if answers == 'да':
            response.set.text(
                'Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по '
                'полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. На всех '
                'секторах игрового поля отмечены инструкции к дальнейшим действиям. \n Покупка недвижимости: Если '
                'вы остановились на поле недвижимости и оно не занято другими участниками, у вас есть право на '
                'его покупку или отказ от покупки. \n Владение недвижимостью: Владение зданием дает право '
                'взыскивать арендную плату с человека, остановившегося на этом поле.\n «Тюрьма»: Чтобы покинуть '
                'этот сектор, необходимо заплатить штраф в 100 $. \n Если вам не хватает средств на какие-то '
                'обязательные выплаты, вы становитесь банкротом. Вы проигрываете. \n \n \n Готов начать?')
            answers = request.command.lower().strip().replace(' ', '')
            if answers == 'да':
                # game = las_vegas()
                response.set.text('я тут')
                end = -1
        if answers == 'конец':
            response.set.text('как скажешь')
            return response, user_storage
        else:
            response.set.text('Не узнав правила, нет смысла даже пытаться. Может всё-таки прочтешь?')


def handle_dialog(request, response, user_storage):
    # response.user_id
    if request.is_new_session:
        # Это новый пользователь.
        # Инициализируем сессию и поприветствуем его.

        user_storage = {
            "user_id": request.user_id,
            "users_turn": True,
            "users_ships": [4, 3, 3, 2, 2, 2, 1, 1, 1, 1],
            "Target": [],  # список с координатами подбитых клеток текущего корабля
            "users_matrix": [[0 for _ in range(10)] for _ in range(10)],
            "cheating_stage": 0,
            "last_turn": None,
            "last_turn_field": [],
            "directions": [[0, 1], [1, 0], [-1, 0], [0, -1]]
        }

        global backup_turn

        backup_turn = user_storage

        # Приветствие
        response.set_text('Привет! Играем в морской бой. Каждая клетка обозначается алфавитной буквой по горизонтали '
                          '(от "А" до "К", исключая "Ё" и "Й", слева направо) и цифрой по вертикали '
                          '(от 1 до 10 сверху вниз). Мои корабли уже расставлены. По вашей готовности атакуйте. Чтобы '
                          'провести атаку скажите или введите координаты.'
                          'Для отмены действия наберите "Отменить"'
                          'Для начала новой игры наберите "Новая игра" или "Выход"')
        # Выходим из функции и ждем ответа
        return response, user_storage

    SHIPS = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    LIFE = sum(SHIPS)
    ALPHABET = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'к']

    KILLED_WORDS = ['убила', 'убил', 'потопила', 'потоплен', 'потопил']
    INJURED_WORDS = ['попала', 'попал', 'попадание', 'ранил', 'ранила', 'ранен']
    MISSED_WORDS = ['мимо', 'промах', 'промазала', 'промазал']
    CANCEL_WORD = ['отмена', 'отменить', 'отменитьход', 'назад']
    ENDING_WORDS = ['новаяигра', 'выход', 'начатьновуюигру', 'начать']

    ALL_WORDS = KILLED_WORDS + INJURED_WORDS + MISSED_WORDS + CANCEL_WORD + ENDING_WORDS

    PHRASES_FOR_ALICES_TURN = ['Пожалуйста, не жульничайте, я контролирую игру.', 'Помоему, сейчас не ваш ход.',
                               'Со мной такое не прокатит. Сейчас мой ход.', 'Может вы не будете меня обманывать?',
                               'Давайте я забуду это, а вы ответите еще раз.']

    PHRASES_FOR_USERS_TURN = ['Сейчас ваш ход, не надо поддаваться.',
                              'Может вы что-то перепутали? Сейчас вы атакуете.',
                              'Я конечно не против, но давайте играть по правилам', 'Не люблю лёгкие победы...']

    # Обрабатываем ответ пользователя.
    user_message = request.command.lower().strip().replace(' ', '')

    # Пробуем перевести в координаты (между if и elif нельзя)
    try_to_make_coor = ''.join(findall(r'\w+', user_message))
    matched = match('\w\d0*', try_to_make_coor)

    try:
        # Проверка слова в допустимых словах
        if user_message in ALL_WORDS:

            # Проверка наличия слова в словах об отемене хода
            if user_message in CANCEL_WORD:
                try:
                    user_storage = backup_turn
                    user_storage["users_turn"] = False
                    response.set_text('Предыдущий ваш ход и ход Алисы отменены.')
                except Exception as e:
                    print(e)
                    response.set_text('Невозможно отменить ход')

            # Проверка наличия слова в словах о начале игры
            elif user_message in ENDING_WORDS:
                user_storage = response.set_text('окей,начало')

            # Если ходит Алиса
            elif not user_storage["users_turn"]:

                backup_turn = user_storage

                # Проверка наличия слова в словах о потоплении
                if user_message in KILLED_WORDS:
                    alice_answer = 'убил'
                    response.set_text(alice_answer)

                # Проверка наличия слова в словах о попадании
                elif user_message in INJURED_WORDS:
                    alice_answer = 'ранил'
                    response.set_text(alice_answer)

                # Проверка наличия слова в словах о промахе
                elif user_message in MISSED_WORDS:
                    alice_answer = 'мимо'
                    response.set_text(alice_answer)

                # Проверка наличия слова в словах об отемене хода
                elif user_message in CANCEL_WORD:
                    try:
                        user_storage["alices_matrix"] = user_storage["last_turn_field"][0]
                        user_storage["users_matrix"] = user_storage["last_turn_field"][1]
                        response.set_text('Предыдущий ваш ход и ход Алисы отменены.')
                        user_storage["last_turn_field"] = []
                    except IndexError:
                        response.set_text('Невозможно отменить ход')

                # Проверка наличия слова в словах о начале игры
                elif user_message in ENDING_WORDS:
                    response.set_text('начало игры')

            # Если игрок сказал не в свой ход
            else:
                response.set_text(choice(PHRASES_FOR_USERS_TURN))

        # Если ничему не соответствует
        else:
            response.set_text("Простите, но я вас не поняла.")

    # Выходы из рекурсии
    except NoCellsError:
        response.set_text("Я простреляла все клетки, так что считайте, что я победила.")

    # В любом случае
    return response, user_storage
