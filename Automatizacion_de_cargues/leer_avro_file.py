from fastavro import reader

def read_avro_file(avro_file): 
    with open(avro_file, "rb") as f:
        avro_reader = reader(f)
        for record in avro_reader:
            print(record)

avro_file = "Automatizacion_de_cargues/datos.avro"

read_avro_file(avro_file)