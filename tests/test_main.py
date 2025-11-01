from main import suma, es_par


class TestSuma:
    """Pruebas de la función suma()"""

    def test_suma_positivos(self):
        assert suma(5, 3) == 8.0


class TestEsPar:
    """Pruebas de la función es_par()"""

    def test_par_positivo(self):
        assert es_par(4) is True
