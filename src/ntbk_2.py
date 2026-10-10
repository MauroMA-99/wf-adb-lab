# Databricks notebook source
dbutils.widgets.text('esquema', 'repaso_dev')
esquema = dbutils.widgets.get('esquema')

display(spark.table(f'workspace.{esquema}.marca_despliegue'))