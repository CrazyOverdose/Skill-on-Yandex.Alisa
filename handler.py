from __future__ import unicode_literals
from json import dump
from random import randint, choice
from copy import deepcopy
from re import findall, match
import logging
import random

logging.basicConfig(level=logging.DEBUG)


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
