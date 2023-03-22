import utils # imports the mod file that exist at the same level

data = [
    {
      'Country': 'Colombia',
      'Population': 500
    },
    {
      'Country': 'Bolivia',
      'Population': 300
    }
]

def main():
  keys, values = dict(utils.get_population())
  print(keys, values)

  result = utils.population_by_country(data, 'Colombia')
  print(result)

if __name__ == "__main__": # This validation makes that only this file will be executed if it's run as a script
  main()