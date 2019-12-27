import unittest
import sys
import json

sys.path.append("..")
from las_vegas import handle_dialog
from alice import AliceRequest
from alice import AliceResponse


class Test_1(unittest.TestCase):
    def test_newgame(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "",
                "nlu": {
                    "entities": [],
                    "tokens": []
                },
                "original_utterance": "",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 0,
                "new": True,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 0,
                "new": True,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Добро пожаловать в \"Лас-Вегас\"! Ты пришёл почувствовать себя успешным предпринимателем! \nВ начале игры Алиса и пользователь имеют по 200$. Каждый участник бросает кубик и в "
                          "зависимости от выпавшего количества очков перемещает фишку по полю. За каждый пройденный "
                          "круг банк выплачивает 200$. Ваша цель – не обанкротиться. \n Если вы остановились на поле "
                          "недвижимости и оно не куплено другими участниками, у вас есть право на его покупку или "
                          "отказ от покупки. Владение недвижимостью дает право взыскивать арендную плату с человека, "
                          "остановившегося на этом поле. Если вся недвижимость будет скуплена, стоимость попадания на "
                          "чужую собственность увеличивается в 3 раза. \n\n Если вам не хватает средств на какие-то "
                          "обязательные выплаты, вы становитесь банкротом. На каждой ячейке поля имеется подробная "
                          "информация о действии этой клетки. Для начала своего хода или хода Алисы введите \"го\". Удачи...и пусть она всегда будет с вами."
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, user_storage), "Всё сломалось :))))))")


class Test_2(unittest.TestCase):
    def test_own(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "мое",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "мое"
                    ]
                },
                "original_utterance": "мое",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Собственность Алисы: \n 2. Колесо обозрения \"High Roller\" Цена: 10$ \n \nВаша собственность: "}
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, user_storage), "Всё сломалось :))))))")


class Test_3(unittest.TestCase):
    def test_money(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "деньги",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "деньги"
                    ]
                },
                "original_utterance": "деньги",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 170.0,  # Деньги Пользователя
            "moneyA": 210.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Ваши деньги 170.0 $\nДеньги Алисы 210.0 $"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, user_storage), "Всё сломалось :))))))")


class Test_4(unittest.TestCase):
    def test_map(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "поле",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "поле"
                    ]
                },
                "original_utterance": "поле",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 170.0,  # Деньги Пользователя
            "moneyA": 210.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "1 - Cтарт\n2 - Колесо обозрения \"High Roller\"\n3 - Лучший предприниматель\n4 - Ранчо \"Casa de Shenandoah\"\n5 - Идите на 2 ячейки назад\n6 - Брат за брата\n7 - Плотина Гувера\n 8 - Сломанный холодильник\n9 - Улица Фримонт-стрит\n 10 - Аллея Лас-Вегас\n 11 - Тюрьма\n 12 - Парка развлечений \"Adventuredome\"\n13 - Биржа\n14 - Музей Shelby American\n 15 - Музей атомных испытаний\n 16 - Отправляйтесь на биржу \n17 - Музей Моб\n 18 - Назад в будущее\n19 - Отель-Казино \"Белладжио\"\n20 - Музей Неона\n  21 - Бесплатный ночлег\n22 - Развлекательный комплекс \"Луксор Лас-Вегас\"\n 23 - Отправляйтесь на начало\n24 - Отель-казино \"Париж Лас-Вегас\"\n25 - Отель-казино \"Венецианский Лас-Вегас\"\n26 - Мотель\n 27 - Отель-казино \"Wynn\"\n28 - Развлекательный комплекс \"Сизарс-Пэлас\"\n29 - Лотерея\n 30 - Отель-казино \"Стратосфера Лас-Вегас\"\n31 - Отправляйтесь в тюрьму\n 32 - Часовня цветов\n 33 - Музей мадам Тюссо\n34 - Любая ячейка.\n35 - Ред-Рок-Каньон\n 36 - Идите на 3 ячейки вперед \n37 - Банк\n38 - Национальный парк \"Долина смерти\"\n 39 - Потеря\n40 - Сансет Парк"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, user_storage), "Всё сломалось :))))))")


class Test_5(unittest.TestCase):
    def test_burse(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "биржа",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "биржа"
                    ]
                },
                "original_utterance": "биржа",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 170.0,  # Деньги Пользователя
            "moneyA": 210.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 432.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Сейчас на бирже 432.0 $"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, user_storage), "Всё сломалось :))))))")


class Test_6(unittest.TestCase):
    def test_bank(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "банк",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "банк"
                    ]
                },
                "original_utterance": "банк",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 55.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 64.0,  # вклады алисы (ячейка поля 37)
            "exchange": 432.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Вклады Алисы: 64.0 $\n Ваши вклады 55.0 $"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, user_storage), "Всё сломалось :))))))")


class Test_7(unittest.TestCase):
    def test_place(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "где я",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "где я"
                    ]
                },
                "original_utterance": "где я",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 34,  # Клетка, на которой находится Алиса
            "field_cellU": 9,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Вы находитесь на 9 ячейке \n Алиса на 34"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, user_storage), "Всё сломалось :))))))")


class Test_8(unittest.TestCase):
    def test_rules(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "правила",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "правила"
                    ]
                },
                "original_utterance": "правила",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "В начале игры Алиса и пользователь имеют по 200$. Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. \n Если вы остановились на поле недвижимости и оно не куплено другими участниками, у вас есть право на его покупку или отказ от покупки. Владение недвижимостью дает право взыскивать арендную плату с человека, остановившегося на этом поле. Если вся недвижимость будет скуплена, стоимость попадания на чужую собственность увеличивается в 3 раза. \n\n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь банкротом. На каждой ячейке поля имеется подробная информация о действии этой клетки. Удачи...и пусть она всегда будет с вами."
 }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, user_storage), "Всё сломалось :))))))")


class Test_9(unittest.TestCase):
    def test_rules(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "новая игра",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "новая игра"
                    ]
                },
                "original_utterance": "новая игра",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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
        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Давай напомню правила: В начале игры Алиса и пользователь имеют по 200$. Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. \n Если вы остановились на поле недвижимости и оно не куплено другими участниками, у вас есть право на его покупку или отказ от покупки. Владение недвижимостью дает право взыскивать арендную плату с человека, остановившегося на этом поле. Если вся недвижимость будет скуплена, стоимость попадания на чужую собственность увеличивается в 3 раза. \n\n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь банкротом. На каждой ячейке поля имеется подробная информация о действии этой клетки. Удачи...и пусть она всегда будет с вами."
 }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_10(unittest.TestCase):
    def test_bad(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "несуществующая команда",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "несуществующая команда"
                    ]
                },
                "original_utterance": "несуществующая команда",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Простите, но я вас не поняла."
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, user_storage), "Всё сломалось :))))))")


class Test_11(unittest.TestCase):
    def test_trueschool(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "4",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "4"
                    ]
                },
                "original_utterance": "4",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 18,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 2,  # пользователь попал на "назад в школу"
            "choice": False,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Правильный ответ"
            }
        }

        newuser_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 250.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 18,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_12(unittest.TestCase):
    def test_falseschool(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "0",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "0"
                    ]
                },
                "original_utterance": "0",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 18,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 2,  # пользователь попал на "назад в школу"
            "choice": False,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        newuser_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 18,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Неправильный ответ \n Правильный ответ: 4"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_13(unittest.TestCase):
    def test_bursegive(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "оставить",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "оставить"
                    ]
                },
                "original_utterance": "оставить",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 100.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 13,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 100.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 13,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": True,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Вы оставили 100$ на бирже"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_14(unittest.TestCase):
    def test_bursetake(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "взять",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "взять"
                    ]
                },
                "original_utterance": "взять",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 13,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 100.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": True,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 350.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 13,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Вы взяли 150.0 $ с биржи"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_15(unittest.TestCase):
    def test_bursenothing(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "ничего не делать",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "ничего не делать"
                    ]
                },
                "original_utterance": "ничего не делать",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 13,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 100.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": True,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 13,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 100.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Иногда ничего не делать - лучшее решение"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_16(unittest.TestCase):
    def test_dontgo(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "ничего не делать",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "ничего не делать"
                    ]
                },
                "original_utterance": "ничего не делать",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 34,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 100.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": True,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": False,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 34,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 100.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Ваш ход \n\n Вы остались на месте "
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_17(unittest.TestCase):
    def test_go(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "1",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "1"
                    ]
                },
                "original_utterance": "1",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 34,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 100.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": True,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": False,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 400.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 100.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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
            "anycell2": True

        }

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "\n Вы перешли на ячейку 1\n\n 1. Cтарт \n"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_18(unittest.TestCase):
    def test_bankzero(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "взять",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "взять"
                    ]
                },
                "original_utterance": "взять",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 37,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": True,  # пользователь попал в банк
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

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 37,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Ваши вклады пусты, вам нечего забирать"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_19(unittest.TestCase):
    def test_banktake(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "взять",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "взять"
                    ]
                },
                "original_utterance": "взять",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 37,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": True,  # пользователь попал в банк
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

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 400.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 37,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Вы обналичили 200.0 $ "
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_20(unittest.TestCase):
    def test_banktake(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "50",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "50"
                    ]
                },
                "original_utterance": "50",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 37,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": True,  # пользователь попал в банк
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

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 150.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 37,  # Клетка, на которой находится пользователь
            "bankU": 250.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Вы оставили 50 $ в банке"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_21(unittest.TestCase):
    def test_bankmany(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "350",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "350"
                    ]
                },
                "original_utterance": "350",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 150.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 37,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": True,  # пользователь попал в банк
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

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 150.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 37,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Нехорошо врать, у тебя нет столько денег"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")

class Test_22(unittest.TestCase):
    def test_banknothing(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "ничего",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "ничего"
                    ]
                },
                "original_utterance": "ничего",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 150.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 37,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": True,  # пользователь попал в банк
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

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 150.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 37,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Денюжки греют душу,когда они под рукой, не так ли?"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")

class Test_23(unittest.TestCase):
    def test_buyno(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "купить",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "купить"
                    ]
                },
                "original_utterance": "купить",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 0.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": False,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 40,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": False,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 0.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": False,  # чей ход
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "У вас недостаточно средств "
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_24(unittest.TestCase):
    def test_buy(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "купить",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "купить"
                    ]
                },
                "original_utterance": "купить",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 100.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": False,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 40,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": False,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 1],
            # имущество пользователя
            "moneyU": 40.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": False,  # чей ход
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Поздравляю с приобретением! "
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_25(unittest.TestCase):
    def test_buynothing(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "не надо",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "не надо"
                    ]
                },
                "original_utterance": "не надо",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 100.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": False,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 40,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": False,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 100.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": False,  # чей ход
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Может, это действительно не лучшее вложение денег"
            }
        }

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_26(unittest.TestCase):
    def test_fraw(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "го",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "го"
                    ]
                },
                "original_utterance": "го",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": -1.0,  # Деньги Пользователя
            "moneyA": -1.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": False,  # чей ход
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Победила дружба :3 \n Давай напомню правила: В начале игры Алиса и пользователь имеют по 200$. Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. \n Если вы остановились на поле недвижимости и оно не куплено другими участниками, у вас есть право на его покупку или отказ от покупки. Владение недвижимостью дает право взыскивать арендную плату с человека, остановившегося на этом поле. Если вся недвижимость будет скуплена, стоимость попадания на чужую собственность увеличивается в 3 раза. \n\n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь банкротом. На каждой ячейке поля имеется подробная информация о действии этой клетки. Удачи...и пусть она всегда будет с вами."
}
        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")

class Test_27(unittest.TestCase):
    def test_defeat(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "го",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "го"
                    ]
                },
                "original_utterance": "го",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": -1.0,  # Деньги Пользователя
            "moneyA": 221.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Мне очень жаль, но вы проиграли \nДавай напомню правила: В начале игры Алиса и пользователь имеют по 200$. Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. \n Если вы остановились на поле недвижимости и оно не куплено другими участниками, у вас есть право на его покупку или отказ от покупки. Владение недвижимостью дает право взыскивать арендную плату с человека, остановившегося на этом поле. Если вся недвижимость будет скуплена, стоимость попадания на чужую собственность увеличивается в 3 раза. \n\n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь банкротом. На каждой ячейке поля имеется подробная информация о действии этой клетки. Удачи...и пусть она всегда будет с вами."
 }
        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_28(unittest.TestCase):
    def test_win(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "го",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "го"
                    ]
                },
                "original_utterance": "го",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 21.0,  # Деньги Пользователя
            "moneyA": -1.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": False,  # чей ход
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Поздравляю, вы победили! \n Давай напомню правила: В начале игры Алиса и пользователь имеют по 200$. Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. \n Если вы остановились на поле недвижимости и оно не куплено другими участниками, у вас есть право на его покупку или отказ от покупки. Владение недвижимостью дает право взыскивать арендную плату с человека, остановившегося на этом поле. Если вся недвижимость будет скуплена, стоимость попадания на чужую собственность увеличивается в 3 раза. \n\n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь банкротом. На каждой ячейке поля имеется подробная информация о действии этой клетки. Удачи...и пусть она всегда будет с вами."
}
        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 200.0,  # Деньги Пользователя
            "moneyA": 200.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 1,  # Клетка, на которой находится пользователь
            "bankU": 0.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_29(unittest.TestCase):
    def test_sellA(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "го",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "го"
                    ]
                },
                "original_utterance": "го",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 21.0,  # Деньги Пользователя
            "moneyA": -1.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": False,  # чей ход
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

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Алиса продала свою недвижимость \n 2. Колесо обозрения \"High Roller\" Цена: 10$ \n  за 5 $"
            }
        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 21.0,  # Деньги Пользователя
            "moneyA": 4.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_30(unittest.TestCase):
    def test_sellU(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "2",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "2"
                    ]
                },
                "original_utterance": "2",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 1, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": -1.0,  # Деньги Пользователя
            "moneyA": 12.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": False,  # пользователь попал на биржу
            "prison1": False,  # тюрьма Алисы
            "prison2": False,  # тюрьма пользователя
            "crash": True,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text": "Вы продали свою недвижимость \n 2. Колесо обозрения \"High Roller\" Цена: 10$ \n  за 5 $"
            }
        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 4.0,  # Деньги Пользователя
            "moneyA": 12.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": False,  # чей ход
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

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")


class Test_31(unittest.TestCase):
    def test_help(self):
        request = {
            "meta": {
                "client_id": "ru.yandex.searchplugin/7.16 (none none; android 4.4.2)",
                "interfaces": {
                    "account_linking": {},
                    "payments": {},
                    "screen": {}
                },
                "locale": "ru-RU",
                "timezone": "UTC"
            },
            "request": {
                "command": "го",
                "nlu": {
                    "entities": [],
                    "tokens": [
                        "го"
                    ]
                },
                "original_utterance": "го",
                "type": "SimpleUtterance"
            },
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "version": "1.0"
        }

        user_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 12.0,  # Деньги Пользователя
            "moneyA": 12.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
            "users_turn": True,  # чей ход
            "bank": False,  # пользователь попал в банк
            "property": 0,  # пользователь попал на ячейку недвижимости
            "go": False,  # на любую ячейку
            "school": 0,  # пользователь попал на "назад в школу"
            "choice": False,  # пользователь попал на биржу
            "prison1": True,  # тюрьма Алисы
            "prison2": True,  # тюрьма пользователя
            "crash": False,  # если пользователь почти банкрот
            "anycell1": False,
            "anycell2": False

        }

        response = {
            "version": "1.0",
            "session": {
                "message_id": 1,
                "new": False,
                "session_id": "5635dea0-e8bbe050-16afad5c-75538f9",
                "skill_id": "2e605c0c-cb43-4bc0-bff7-007f695822ad",
                "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403"
            },
            "response": {
                "end_session": False,
                "text":  "Алиса помогла сбежать вам из тюрьмы, ходите "
            }
        }

        newuser_storage = {
            "propertyA": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],  # имущество Алисы
            "propertyU": [2, 2, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 0,
                          0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0],
            # имущество пользователя
            "moneyU": 12.0,  # Деньги Пользователя
            "moneyA": 12.0,  # Деньги Алисы
            "field_cellA": 1,  # Клетка, на которой находится Алиса
            "field_cellU": 40,  # Клетка, на которой находится пользователь
            "bankU": 200.0,  # вклады пользователя (ячейка поля 37)
            "bankA": 0.0,  # вклады алисы (ячейка поля 37)
            "exchange": 0.0,  # деньги на бирже (ячейка поля 13)
            "user_id": "4912D562F9B17A606D7EAB894ED13B0F1B25B342BD3EFD046F887A4FBB52D403",
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

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)

        alice_response, user_storage2 = handle_dialog(
            alice_request, alice_response, user_storage
        )

        json_str = json.dumps(
            response,
            ensure_ascii=False,
            indent=2
        )
        self.assertEqual((alice_response.dumps(), user_storage2), (json_str, newuser_storage), "Всё сломалось :))))))")







