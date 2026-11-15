from exceptions import MatrixDimensionError

def transpose_matrix(matrix):
    """
    Transponuje macierz (zamienia wiersze z kolumnami).

    :param matrix: Macierz jako lista list.
    :return: Transponowana macierz jako lista list.
    """
    return [list(row) for row in zip(*matrix)]


def multiply_matrices(matrix_a, matrix_b):
    """
    Mnoży dwie macierze.

    :param matrix_a: Pierwsza macierz jako lista list.
    :param matrix_b: Druga macierz jako lista list.
    :raises MatrixDimensionError: Jeśli liczba kolumn w matrix_a nie zgadza się z liczbą wierszy w matrix_b.
    :return: Wynik mnożenia jako lista list.
    """
    if len(matrix_a[0]) != len(matrix_b):
        raise MatrixDimensionError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej macierzy.")
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix_b)] for row in matrix_a]
