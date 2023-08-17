import utils
import read_csv
import graficas



def run():

  data = read_csv.read_csv('./app/world_population.csv')
  data = list(filter(lambda item:item['Continent'] == 'South America', data))
  countries = list(map(lambda x:x['Country/Territory'], data))
  percentages = list(map(lambda x:x['World Population Percentage'], data))

  graficas.generate_pie_char(countries, percentages)
  """ 
  country = input("ingrese el pais").title()

  result = utils.get_population_by_country(data, country)
  if len(result)>0:
    country = result[0]
    labels, values = utils.get_popullation(country)
    graficas.generate_bar_char(labels, values)
 """
  print(utils.get_population_by_country(countries, percentages))
  #Example.py controla la ejecución de main.py, pero si desde la terminal tratamos de 
#ejecutar main.py no va a funcionar
#A eso se le llama dualidad
#para solucionarlo se agrega la siguiente linea en main 
 
if __name__ == '__main__': 
  run()