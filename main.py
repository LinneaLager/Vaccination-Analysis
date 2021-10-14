# import argparse method
import argparse
# import datahandler class and methods
from datahandler import PlotVaccinations as pv

# Creating argument that will be parsed by user
parser = argparse.ArgumentParser(description='This application compares two countries in terms of vaccination data, you can select the vaccination numbers you would like to compare between the countries')
parser.add_argument('-c1','--country1',type=str,required=True, help = 'First country to analyse')
parser.add_argument('-c2','--country2',type=str,required=False,help = 'Second country to analyse (optional)')
parser.add_argument('-d','--dataflag',type=str,required=True,
                    help = 'Select the field you would like to analyse: total_vaccinations,people_fully_vaccinated, daily_vaccinations, total_vaccinations_per_hundred, people_fully_vaccinated_per_hundred')
args = parser.parse_args()

if __name__ == '__main__':

    if args.country2 is None:
        pv(args.country1, 'undefined' , args.dataflag)
    else:
        pv(args.country1, args.country2, args.dataflag)
