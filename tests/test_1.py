import unittest
from alice import AliceResponse
from alice import AliceRequest
from las_vegas import handle_dialog

class Test(unittest.TestCase):

    def test_rules(self):
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
            {
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
        }

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

        alice_request = AliceRequest(request)

        ##Ответ Алисы пользователю
        alice_response = AliceResponse(alice_request)


        alice_response, user_storage = handle_dialog(
            alice_request, alice_response, user_storage
        )

        self.assertEqual(alice_response.dumps(), response, "Всё совпало")


