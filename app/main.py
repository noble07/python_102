import utils # imports the mod file that exist at the same level
import read_csv
import charts

def main():
    data = read_csv.read_csv("./app/data.csv")
    country = input("Type Country => ")

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
    
    c_name, per = utils.get_world_percentages(data)
    charts.generate_pie_chart(c_name, per)

if __name__ == "__main__": # This validation makes that only this file will be executed if it's run as a script
  main()