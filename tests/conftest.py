import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope='session')
def spark():
    sesion = (SparkSession.builder
              .master('local[1]')
              .appName('pruebas')
              .config('spark.sql.shuffle.partitions', '1')
              .getOrCreate())
    yield sesion
    sesion.stop()
    
    