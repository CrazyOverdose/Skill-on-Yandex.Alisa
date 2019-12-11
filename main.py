"""coding: utf-8
Импортирует поддержку UTF-8."""
from __future__ import unicode_literals

"""Импортируем модули для работы с логами"""
import logging

"""Импортируем модуль для работы с json"""
import json

"""Импортируем модуль для работы с API Алисы"""
from alice import AliceRequest, AliceResponse

"""Импортируем модуль с логикой игры"""
from las_vegas import handle_dialog

"""Импортируем подмодули Flask для запуска веб-сервиса."""
from flask import Flask, request


##Экземпляр Flask класса, в который передается имя модуля и пакета
app = Flask(__name__)

##Создание лога (отладочное сообщение)
logging.basicConfig(level=logging.DEBUG)

##Хранение сессии
session_storage = {}

##Стандарт кодирования символов
with open("sessions.json", "w", encoding="utf8") as file:
    json.dump(session_storage, fp=file)

##Параметры приложения Flask. Браузер сообщает серверу, что хочет запостить новую информацию по данному URL и сервер должен быть уверен, что сохранит ее и сделает один раз.
@app.route("/", methods=["POST"])

##Функция, обрабатывающая запрос пользователя и возвращающая ответ
def main():
    with open("sessions.json", encoding="utf8") as file:
        session_storage = json.loads(file.read())

    ##Запрос пользователя к Алисе
    alice_request = AliceRequest(request.json)

    ##Ответ Алисы пользователю
    alice_response = AliceResponse(alice_request)

    ##Идентификатор экземпляра приложения, в котором пользователь общается с Алисой, максимум 64 символа.
    user_id = alice_request.user_id

    alice_response, session_storage[user_id] = handle_dialog(
        alice_request, alice_response, session_storage.get(user_id)
    )

    with open("sessions.json", "w", encoding="utf8") as file:
        json.dump(session_storage, fp=file)

    logging.info("Response: {}".format(alice_response))

    return alice_response.dumps()


if __name__ == '__main__':
    ##Запуск локального сервера
    app.run()
