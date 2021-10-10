## Vaccination-Analysis

# Hi and welcome to the Vaccination analysis application!

This application compares two countries in terms of vaccination data, you can select the vaccination numbers you would
like to compare between the countries. For each country or two countries you can analyse the following columns.

total_vaccinations <br/>
people_vaccinated <br/>
people_fully_vaccinated <br/>
daily_vaccinations_raw <br/>
daily_vaccinations <br/>
total_vaccinations_per_hundred <br/>
people_vaccinated_per_hundred <br/>
people_fully_vaccinated_per_hundred <br/> 
daily_vaccinations_per_million <br/>

If you need additional information such as the sources for each individual country then you can find them in the excel-document. 

The different columns stated above can be sorted and compared for two countries in a simple bar-chart. For some help enter -h. 

# Instructions!

Download or clone repository. Use pip install -r requirements.txt. What to enter into the terminal? 
    
    python main.py -c1 country1 -c2 country2 -d datacolumn 
    
If you only want to analyse just one country then don't enter the -c2.


