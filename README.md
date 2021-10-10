## Vaccination-Analysis-Linnea

# Hi and welcome to Vaccination analysis!

This application compares two countries in terms of vaccination data, you can select the vaccination numbers you would
like to compare between the countries.

optional arguments:
  -h, --help            show this help message and exit
  -c1 COUNTRY1, --country1 COUNTRY1
                        First country to analyse
  -c2 COUNTRY2, --country2 COUNTRY2
                        Second country to analyse (optional)
  -d DATAFLAG, --dataflag DATAFLAG
                        Select the field you would like to analyse: total_vaccinations, people_vaccinated,
                        people_fully_vaccinated, daily_vaccinations_raw, daily_vaccinations,
                        total_vaccinations_per_hundred, people_vaccinated_per_hundred,
                        people_fully_vaccinated_per_hundred, daily_vaccinations_per_million

The different columns stated above can be sorted and compared for two countries in a simple bar-chart. 

# Instructions!

Download or clone repository. Use pip install -r requirements.txt. What to enter into the terminal? 
    
    python main.py -c1 country1 -c2 country2 -d datacolumn 
    
If you only want to analyse just one country then don't enter the -c2.


