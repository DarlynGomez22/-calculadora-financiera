# Calculadora Financiera - TDD + CI

Módulo de operaciones financieras desarrollado aplicando **TDD (Red-Green-Refactor)** e **Integración Continua** con GitHub Actions.

## Funciones

- `interes_simple(capital, tasa, tiempo)` → I = C × r × t
- `interes_compuesto(capital, tasa, periodos)` → M = C × (1 + r)^n
- `cuota_prestamo(monto, tasa, n)` → Cuota fija (sistema francés)
- `valor_presente(valor_futuro, tasa, n)` → VP = VF / (1 + r)^n
- `valor_futuro(pago, tasa, n)` → Anualidad
- `descuento(precio, porcentaje)` → Precio con descuento

## Instalación

```bash
git clone https://github.com/tu-usuario/calculadora-financiera.git
cd calculadora-financiera
pip install -r requirements.txt