from pyspark.sql import functions as F


def clasificar_monto(df):
    """Agrega la columna 'categoria' segun el monto del pedido."""
    return df.withColumn(
        'categoria',
        F.when(F.col('monto') >= 1000, 'alto')
         .when(F.col('monto') >= 10, 'medio')
         .otherwise('bajo')
    )
    