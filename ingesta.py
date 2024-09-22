import boto3
import pandas as pd
import mysql.connector

def mysql_to_csv(host, port, user, password, database, table, ficheroUpload):
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    query = f"SELECT * FROM {table}"
    df = pd.read_sql(query, connection)
    df.to_csv(ficheroUpload, index=False)

    connection.close()

ficheroUpload = "data.csv"
nombreBucket = "nsy-output-s3b"

mysql_to_csv('100.27.161.243', '8005', 'root', 'utec', 'tienda', 'fabricantes', ficheroUpload)

res = boto3.client('s3').upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print("Ingesta completada")
