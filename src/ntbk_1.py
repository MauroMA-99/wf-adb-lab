# Databricks notebook source
dbutils.widgets.text('esquema', 'repaso_dev')
esquema = dbutils.widgets.get('esquema')

spark.sql(f'CREATE SCHEMA IF NOT EXISTS workspace.{esquema}')
spark.sql(f"""
CREATE OR REPLACE TABLE workspace.{esquema}.marca_despliegue AS
SELECT current_timestamp() AS momento, '{esquema}' AS entorno, 'v1' AS version_codigo
""")
print(f'ntbk_1 escribió en workspace.{esquema}')