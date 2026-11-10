"""
Pruebas unitarias de la Calculadora Financiera.
Escritas ANTES de la implementación (ciclo TDD - Red fase).
"""
import pytest
from src.calculadora import (
    interes_simple,
    interes_compuesto,
    cuota_prestamo,
    valor_presente,
    valor_futuro,
    descuento,
)


# ---------- Interés simple ----------
class TestInteresSimple:
    def test_calculo_basico(self):
        # C=1000, r=0.05, t=2 → I = 100
        assert interes_simple(1000, 0.05, 2) == pytest.approx(100.0, abs=0.01)

    def test_tasa_cero(self):
        assert interes_simple(1000, 0.0, 5) == pytest.approx(0.0)

    def test_capital_negativo_lanza_error(self):
        with pytest.raises(ValueError):
            interes_simple(-100, 0.05, 2)

    def test_tasa_negativa_lanza_error(self):
        with pytest.raises(ValueError):
            interes_simple(1000, -0.05, 2)

    def test_tiempo_negativo_lanza_error(self):
        with pytest.raises(ValueError):
            interes_simple(1000, 0.05, -1)


# ---------- Interés compuesto ----------
class TestInteresCompuesto:
    def test_calculo_basico(self):
        # 1000 * (1.1)^2 = 1210
        assert interes_compuesto(1000, 0.10, 2) == pytest.approx(1210.0, abs=0.01)

    def test_tasa_cero(self):
        assert interes_compuesto(1000, 0.0, 5) == pytest.approx(1000.0)

    def test_un_periodo(self):
        # 1000 * 1.05 = 1050
        assert interes_compuesto(1000, 0.05, 1) == pytest.approx(1050.0, abs=0.01)

    def test_capital_negativo_lanza_error(self):
        with pytest.raises(ValueError):
            interes_compuesto(-1000, 0.10, 2)


# ---------- Cuota de préstamo ----------
class TestCuotaPrestamo:
    def test_calculo_basico(self):
        # Préstamo 10000, tasa mensual 1%, 12 meses → cuota ≈ 888.49
        assert cuota_prestamo(10000, 0.01, 12) == pytest.approx(888.49, abs=0.01)

    def test_tasa_cero(self):
        # Sin interés, cuota = monto / n
        assert cuota_prestamo(1200, 0.0, 12) == pytest.approx(100.0, abs=0.01)

    def test_periodos_cero_lanza_error(self):
        with pytest.raises(ValueError):
            cuota_prestamo(10000, 0.01, 0)

    def test_monto_negativo_lanza_error(self):
        with pytest.raises(ValueError):
            cuota_prestamo(-1000, 0.01, 12)


# ---------- Valor presente ----------
class TestValorPresente:
    def test_calculo_basico(self):
        # VF=1210, r=0.10, n=2 → VP = 1000
        assert valor_presente(1210, 0.10, 2) == pytest.approx(1000.0, abs=0.01)

    def test_tasa_cero(self):
        assert valor_presente(1000, 0.0, 5) == pytest.approx(1000.0)

    def test_periodos_negativos_lanza_error(self):
        with pytest.raises(ValueError):
            valor_presente(1210, 0.10, -1)


# ---------- Valor futuro ----------
class TestValorFuturo:
    def test_calculo_basico(self):
        # P=100, r=0.05, n=3 → VF ≈ 315.25
        assert valor_futuro(100, 0.05, 3) == pytest.approx(315.25, abs=0.01)

    def test_tasa_cero(self):
        # Sin interés, VF = pago * n
        assert valor_futuro(100, 0.0, 5) == pytest.approx(500.0, abs=0.01)

    def test_pago_negativo_lanza_error(self):
        with pytest.raises(ValueError):
            valor_futuro(-100, 0.05, 3)


# ---------- Descuento ----------
class TestDescuento:
    def test_calculo_basico(self):
        # 200 * (1 - 0.15) = 170
        assert descuento(200, 0.15) == pytest.approx(170.0, abs=0.01)

    def test_sin_descuento(self):
        assert descuento(200, 0.0) == pytest.approx(200.0)

    def test_descuento_total(self):
        assert descuento(200, 1.0) == pytest.approx(0.0)

    def test_porcentaje_invalido_lanza_error(self):
        with pytest.raises(ValueError):
            descuento(100, 1.5)

    def test_porcentaje_negativo_lanza_error(self):
        with pytest.raises(ValueError):
            descuento(100, -0.1)

    def test_precio_negativo_lanza_error(self):
        with pytest.raises(ValueError):
            descuento(-50, 0.10)
        