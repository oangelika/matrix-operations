class MatrixDimensionError(Exception):
    """
    Wyjątek zgłaszany, gdy wymiary macierzy nie pozwalają na ich mnożenie.
    """
    def __init__(self, message="Nieprawidłowe wymiary macierzy do mnożenia."):
        self.message = message
        super().__init__(self.message)
