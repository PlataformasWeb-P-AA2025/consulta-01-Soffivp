import pandas as pd
from pymongo import MongoClient

# Configuración de conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['demo']  # Nombre de tu base de datos

# Leer el archivo Excel
excel_file = 'data/2022.xlsx'
#excel_file = 'data/2023.xlsx'
df = pd.read_excel(excel_file)

# Convertir el DataFrame a diccionario para MongoDB
data = df.to_dict('records')

# Insertar los datos en una colección (elige un nombre)
collection_name = 'datos'  # Puedes cambiar este nombre
db[collection_name].insert_many(data)

print(f"Se insertaron {len(data)} documentos en la colección '{collection_name}'")



# Consulta básica


# Filtramos los partidos que fueron en Cuartos de finales

resultados = list(db.datos.find({"Round": "Quarterfinals"}))

# Mostrar resultados simplificados
for doc in resultados:

    print(doc)


   


#cuanta de victorias de un elemento en especifico 
num_victorias = db.datos.count_documents({"Winner": "Draper J."})
print("--------------------Total de Victorias de Draper J.------------------------")
print(f"Draper J. tiene {num_victorias} victorias registradas")

