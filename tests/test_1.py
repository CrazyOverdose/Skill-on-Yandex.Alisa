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
                "text": "Добро пожаловать в \"Лас-Вегас\"! Ты пришёл почувствовать себя успешным предпринимателем! Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. \n Если вы остановились на поле недвижимости и оно не куплено другими участниками, у вас есть право на его покупку или отказ от покупки. \n Владение недвижимостью дает право взыскивать арендную плату с человека, остановившегося на этом поле.\n\n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь банкротом. \n Посмотреть все доступные команды: \"команды\" \n Начать игру: \"бросить кубик\""

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
                "text": "Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. \n Если вы остановились на поле недвижимости и оно не занято другими участниками, у вас есть право на его покупку или отказ от покупки. \n Владение зданием дает право взыскивать арендную плату с человека, остановившегося на этом поле.\n «Тюрьма»: Попав на эту ячейку, вы теряете 150$ и пропускаете ход \n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь банкротом. \n \n Чтобы начать игру \"бросить кубик\""
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


class Test_3(unittest.TestCase):
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


class Test_4(unittest.TestCase):
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


class Test_5(unittest.TestCase):
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


class Test_6(unittest.TestCase):
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


class Test_7(unittest.TestCase):
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


class Test_8(unittest.TestCase):
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
                "text": "Каждый участник бросает кубик и в зависимости от выпавшего количества очков перемещает фишку по полю. За каждый пройденный круг банк выплачивает 200$. Ваша цель – не обанкротиться. \n Если вы остановились на поле недвижимости и оно не куплено другими участниками, у вас есть право на его покупку или отказ от покупки. \n Владение зданием дает право взыскивать арендную плату с человека, остановившегося на этом поле.\n \n Если вам не хватает средств на какие-то обязательные выплаты, вы становитесь банкротом. \n \n Чтобы посмотреть все доступные команды: \"команды\" \n Чтобы начать игру: \"бросить кубик\""
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

