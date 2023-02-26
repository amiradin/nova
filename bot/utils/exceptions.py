class ParseException(Exception):
    """
    Исключение при парсинге данных
    """

    def __init__(self, message="Некорректный формат данных"):
        self.message = message
        super().__init__(self.message)
