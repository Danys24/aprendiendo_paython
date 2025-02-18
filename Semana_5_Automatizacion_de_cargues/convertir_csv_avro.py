import pandas as pd
import csv
from fastavro import writer as wr

schema = {
    "type" : "record",
    "name" : "CSVtoAvro",
    "fields" : [
        {"name": "NOMBRE", "type" : "string"},
        {"name": "EDAD", "type" : "int"},
        {"name": "CARRERA_PROFESIONAL", "type" : "string"},
        {"name": "CIUDAD", "type" : "string"}
    ]
}

def csv_a_avro(csv_file, avro, schema):
    with open(csv_file, "r") as csv_f: 
        csv_reader = csv.DictReader(csv_f)
        records = []

        for row in csv_reader:
            record = {
                "NOMBRE": row["NOMBRE"],
                "EDAD": int(row["EDAD"]),
                "CARRERA_PROFESIONAL": row["CARRERA_PROFESIONAL"],
                "CIUDAD": row["CIUDAD"]
            }
            records.append(record)

    with open(avro, "wb") as avro_f:
        wr(avro_f, schema, records)

csv_file = "Semana_5_Automatizacion_de_cargues/datos_2.csv"
avro_file = "Semana_5_Automatizacion_de_cargues/datos.avro"

csv_a_avro(csv_file, avro_file, schema)

print(f"archivo Avro generado: {avro_file}")

#data = pd.read_csv("datos_2.csv")
#print(data)