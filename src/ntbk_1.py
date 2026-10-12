# Databricks notebook source
import sys
sys.path.append('..')

from utils.transformaciones import clasificar_monto

dbutils.widgets.text('esquema', 'repaso_dev')
esquema = dbutils.widgets.get('esquema')

spark.sql(f'CREATE SCHEMA IF NOT EXISTS workspace.{esquema}')

pedidos = spark.createDataFrame(
    [(1, 2500.0), (2, 500.0), (3, 50.0), (4, 1200.0)],
    'id_pedido INT, monto DOUBLE')

clasificado = clasificar_monto(pedidos)
clasificado.write.mode('overwrite').saveAsTable(f'workspace.{esquema}.pedidos_clasificados')

spark.sql(f"""
CREATE OR REPLACE TABLE workspace.{esquema}.marca_despliegue AS
SELECT current_timestamp() AS momento, '{esquema}' AS entorno, 'v1' AS version_codigo
""")

print(f'ntbk_1 escribio en workspace.{esquema}')
