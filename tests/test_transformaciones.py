import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.utils.transformaciones import clasificar_monto


def test_clasifica_las_tres_categorias(spark):
    datos = spark.createDataFrame(
        [(1, 2500.0), (2, 500.0), (3, 50.0)],
        'id INT, monto DOUBLE')

    filas = clasificar_monto(datos).orderBy('id').collect()

    assert filas[0]['categoria'] == 'alto'
    assert filas[1]['categoria'] == 'medio'
    assert filas[2]['categoria'] == 'bajo'


def test_los_limites_exactos(spark):
    datos = spark.createDataFrame(
        [(1, 1000.0), (2, 999.99), (3, 100.0), (4, 99.99)],
        'id INT, monto DOUBLE')

    filas = clasificar_monto(datos).orderBy('id').collect()

    assert filas[0]['categoria'] == 'alto'
    assert filas[1]['categoria'] == 'medio'
    assert filas[2]['categoria'] == 'medio'
    assert filas[3]['categoria'] == 'bajo'


def test_monto_nulo_cae_en_bajo(spark):
    datos = spark.createDataFrame([(1, None)], 'id INT, monto DOUBLE')

    filas = clasificar_monto(datos).collect()

    assert filas[0]['categoria'] == 'bajo'
    