"""
Calculadora Financiera - Módulo de operaciones financieras básicas.
Desarrollado aplicando TDD (Red-Green-Refactor).
"""


def _validar_positivo(valor: float, nombre: str) -> None:
    """Valida que un valor numérico no sea negativo."""
    if valor < 0:
        raise ValueError(f"{nombre} no puede ser negativo")


def _validar_tasa(tasa: float) -> None:
    """Valida que la tasa esté en un rango razonable."""
    if tasa < 0:
        raise ValueError("La tasa no puede ser negativa")


def interes_simple(capital: float, tasa: float, tiempo: float) -> float:
    """
    Calcula el interés simple: I = C * r * t

    :param capital: Capital inicial (C)
    :param tasa: Tasa de interés por período (r), expresada en decimal (0.05 = 5%)
    :param tiempo: Número de períodos (t)
    :return: Interés generado
    """
    _validar_positivo(capital, "capital")
    _validar_tasa(tasa)
    _validar_positivo(tiempo, "tiempo")
    return round(capital * tasa * tiempo, 2)


def interes_compuesto(capital: float, tasa: float, periodos: int) -> float:
    """
    Calcula el monto final con interés compuesto: M = C * (1 + r)^n

    :param capital: Capital inicial (C)
    :param tasa: Tasa de interés por período (r), en decimal
    :param periodos: Número de períodos (n)
    :return: Monto final
    """
    _validar_positivo(capital, "capital")
    _validar_tasa(tasa)
    _validar_positivo(periodos, "periodos")
    return round(capital * (1 + tasa) ** periodos, 2)


def cuota_prestamo(monto: float, tasa: float, n: int) -> float:
    """
    Calcula la cuota fija de un préstamo (sistema francés):
    Cuota = M * r / (1 - (1 + r)^(-n))

    :param monto: Monto del préstamo
    :param tasa: Tasa de interés por período, en decimal
    :param n: Número de períodos (cuotas)
    :return: Valor de la cuota fija
    """
    _validar_positivo(monto, "monto")
    _validar_tasa(tasa)
    if n <= 0:
        raise ValueError("El número de períodos debe ser mayor que cero")

    if tasa == 0:
        return round(monto / n, 2)

    cuota = monto * tasa / (1 - (1 + tasa) ** (-n))
    return round(cuota, 2)


def valor_presente(valor_futuro_: float, tasa: float, n: int) -> float:
    """
    Calcula el valor presente: VP = VF / (1 + r)^n

    :param valor_futuro_: Valor futuro (VF)
    :param tasa: Tasa de interés por período, en decimal
    :param n: Número de períodos
    :return: Valor presente
    """
    _validar_tasa(tasa)
    if n < 0:
        raise ValueError("El número de períodos no puede ser negativo")
    return round(valor_futuro_ / (1 + tasa) ** n, 2)


def valor_futuro(pago: float, tasa: float, n: int) -> float:
    """
    Calcula el valor futuro de una anualidad: VF = P * [((1+r)^n - 1) / r]

    :param pago: Pago periódico (P)
    :param tasa: Tasa de interés por período, en decimal
    :param n: Número de períodos
    :return: Valor futuro de la anualidad
    """
    _validar_positivo(pago, "pago")
    _validar_tasa(tasa)
    if n < 0:
        raise ValueError("El número de períodos no puede ser negativo")

    if tasa == 0:
        return round(pago * n, 2)

    vf = pago * (((1 + tasa) ** n - 1) / tasa)
    return round(vf, 2)


def descuento(precio: float, porcentaje: float) -> float:
    """
    Calcula el precio final tras aplicar un descuento.

    :param precio: Precio original
    :param porcentaje: Porcentaje de descuento en decimal (0.15 = 15%)
    :return: Precio con descuento aplicado
    """
    _validar_positivo(precio, "precio")
    if not 0 <= porcentaje <= 1:
        raise ValueError("El porcentaje debe estar entre 0 y 1")
    return round(precio * (1 - porcentaje), 2)