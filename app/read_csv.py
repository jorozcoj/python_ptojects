import csv

def read_csv(path): 
    with open(path, 'r', encoding="UTF-8") as csvfile:
        reade = csv.reader(csvfile, delimiter=',') 
        header = next(reade) #en el header se lee manualmente la primer linea del archivo
        data = []
        #print(header) # Se obtiene un array solo con los nombres que tendriamos para el diccionario
        #despues de tener el lector, se hace un iterador para leer fila x fila
        for row in reade:
            iterable = zip(header, row)
            country_dict = {key:value for key, value in iterable}
            data.append(country_dict)
        return data
if __name__ =='__main__':
    data = read_csv('./app/world_population.csv')
    print(data[0])

#tenemos que transformarlo en diccionario para poderlo leer mas facilmente