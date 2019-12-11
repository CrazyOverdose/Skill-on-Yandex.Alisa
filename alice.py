import json


class AliceRequest(object):
    """Класс, обрабатывающий запрос к Алисе."""

    def __init__(self, request_dict):
        """Конструктор класса"""
        self._request_dict = request_dict

    @property
    def version(self):
        """Версия протокола. Текущая версия - 1.0"""
        return self._request_dict['version']

    @property
    def session(self):
        """Данные о сессии"""
        return self._request_dict['session']

    @property
    def user_id(self):
        """Идентификатор экземпляра приложения, в котором
    пользователь общается с Алисой, максимум 64 символа."""
        return self.session['user_id']

    @property
    def is_new_session(self):
        """Признак новой сессии.
        Возможные значения:
        1. true - пользователь начинает новый разговор с навыком Алисы
        2. false - запрос отправлен в рамках уже начатого разговора"""
        return bool(self.session['new'])

    @property
    def command(self):
        """Служебное поле: запрос пользователя,
    преобразованный для внутренней обработки Алисы. В ходе преобразования текст, в частности, очищается от знаков
    препинания, а числительные преобразуются в числа."""
        return self._request_dict['request']['command']

    def __str__(self):
        """Метод получения строкового представления объекта."""
        return str(self._request_dict)


class AliceResponse(object):
    """Класс - ответ Алисы пользователю."""

    def __init__(self, alice_request):
        """Формат ответа Алисы пользователю"""
        self._response_dict = {
            "version": alice_request.version,
            "session": alice_request.session,
            "response": {
                "end_session": False
            }
        }

    def dumps(self):
        """Сериализует в строку JSON - формата"""
        return json.dumps(
            self._response_dict,
            ensure_ascii=False,
            indent=2
        )

    def set_text(self, text):
        """Текст, который получит пользователь от Алисы. Максимум 1024 символа. Не должен быть пустым."""
        self._response_dict['response']['text'] = text[:1024]

    def end(self):
        """Признак конца диалога"""
        self._response_dict["response"]["end_session"] = True

    def __str__(self):
        """Метод получения строкового представления объекта."""
        return self.dumps()
