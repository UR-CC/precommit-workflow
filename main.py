def suma(a: float, b: float) -> float:
    """
    Calcula la suma de dos números

    Args:
        a (float): primer número para sumar
        b (float): segundo número para sumar

    Returns:
        float: el resultado de la suma de a + b

    Examples:
        >>> suma(5, 3)
        8.0
        >>> suma(-1, 1)
        0.0
    """
    return float(a + b)


def es_par(n: int) -> bool:
    """
    Determina si un número es par

    Args:
        n (int): número a evaluar

    Returns:
        bool: True si el número es par, y False si es impar

    Examples:
        >>> es_par(4)
        True
        >>> es_par(9)
        False
    """
    return (n % 2) == 0


if __name__ == "__main__":
    print(f"la suma de 5 + 3 = {suma(5, 3)}")
    print(f"el número 4 es par? {es_par(4)}")
    print(f"el número 9 es par? {es_par(9)}")
